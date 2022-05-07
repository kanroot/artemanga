from django.http import Http404

class ErrorBase(Exception):
    pass

class PaginaPreviaNoPermitida(Http404):
    def __init__(self, pagina: str):
        super().__init__(f'Se hizo intento de acceder a página que no admite acceso sin redirección exacta: {pagina}')