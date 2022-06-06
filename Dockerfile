FROM python:3.10.4-alpine3.15

# enables proper stdout flushing
ENV PYTHONUNBUFFERED yes
# no .pyc files
ENV PYTHONDONTWRITEBYTECODE yes

# pip optimizations
ENV PIP_NO_CACHE_DIR yes
ENV PIP_DISABLE_PIP_VERSION_CHECK yes

WORKDIR /src

COPY poetry.lock pyproject.toml ./

RUN apk add --no-cache libpq \
    && apk add --no-cache --virtual .build-deps \
    gcc \
    musl-dev \
    python3-dev \
    libffi-dev \
    openssl-dev \
    cargo \
    postgresql-dev \
    jpeg-dev \
    libjpeg \
    zlib-dev \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev \
    && apk del --purge .build-deps \
    && apk add libjpeg

COPY src .

RUN mkdir /home/website
RUN mkdir /home/website/statics
RUN mkdir /home/website/media
RUN mkdir /home/website/logs

RUN sed -i 's/\r$//g' entrypoint.sh
RUN chmod +x entrypoint.sh

# corre el comando de enviar correos cada minuto
RUN crontab -l | { cat; echo "* * * * * python /src/manage.py send_queued_mail >> /home/website/logs/send_mail.log 2>&1"; } | crontab -
# corre comando para auto-expirar campañas cada 10 minutos
RUN crontab -l | { cat; echo "*/10 * * * * python /src/manage.py revisar_expiracion_campannas" ; } | crontab -

ENTRYPOINT ["./entrypoint.sh"]