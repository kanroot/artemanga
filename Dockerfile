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
    # https://cryptography.io/en/latest/installation/#alpine
    gcc \
    musl-dev \
    python3-dev \
    libffi-dev \
    openssl-dev \
    cargo \
    postgresql-dev \
    jpeg-dev \
    zlib-dev \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev \
    && apk del --purge .build-deps

COPY src .

RUN mkdir /home/website
RUN mkdir /home/website/statics
RUN mkdir /home/website/media

RUN sed -i 's/\r$//g' entrypoint.sh
RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]