from dataclasses import dataclass, field, asdict
from urllib.parse import urlparse

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import redirect_to_login
from django.shortcuts import resolve_url
from django.urls import reverse_lazy
from artemangaweb.exceptions import PaginaPreviaNoPermitida

from cuenta_usuario.enums.opciones import TipoUsuario


class MensajeResultadoFormMixin:
    mensaje_exito = 'Operación realizada con éxito'
    mensaje_error = 'Operación ha fallado'

    def get_mensaje_exito(self):
        return self.mensaje_exito

    def get_mensaje_error(self):
        return self.mensaje_error

    def form_valid(self, form):
        messages.success(self.request, self.mensaje_exito)
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, self.mensaje_error)
        return super().form_invalid(form)


class TituloPaginaMixin:
    titulo_pagina = None

    def get_titulo_pagina(self):
        return self.titulo_pagina

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_pagina"] = self.get_titulo_pagina()

        return context


class VistaRestringidaMixin(LoginRequiredMixin):
    usuarios_permitidos: list[TipoUsuario] = [TipoUsuario.ADMINISTRADOR]
    login_url = reverse_lazy('login')
    permission_denied_message = 'No tiene permisos para acceder a esta página. ' \
                                'Si crees que deberías, por favor contacta al administrador de sistema.'

    todos_los_usuarios = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA, TipoUsuario.VENTAS, TipoUsuario.CLIENTE]
    todos_los_administradores = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA, TipoUsuario.VENTAS]

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if request.user.tipo_usuario not in self.valores_usuarios_permitidos:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        path = self.request.build_absolute_uri()
        resolved_login_url = resolve_url(self.get_login_url())
        # If the login url is the same scheme and net location then use the
        # path as the "next" url.
        login_scheme, login_netloc = urlparse(resolved_login_url)[:2]
        current_scheme, current_netloc = urlparse(path)[:2]
        if (not login_scheme or login_scheme == current_scheme) and (
            not login_netloc or login_netloc == current_netloc
        ):
            path = self.request.get_full_path()
        return redirect_to_login(
            path,
            resolved_login_url,
            self.get_redirect_field_name(),
        )

    @property
    def valores_usuarios_permitidos(self):
        return [tipo.value for tipo in self.usuarios_permitidos]


class ImpedirSinRedireccionMixin:
    """
    Mixin que impide que se pueda acceder a una vista si no viene de una redirección.
    Es posible sobrescribir ``paginas_permitidas`` para definir exactamente qué páginas se permiten.
    """
    paginas_permitidas = ["*"]

    def dispatch(self, request, *args, **kwargs):
        pagina_anterior = request.META.get('HTTP_REFERER', )

        if not pagina_anterior:
            raise PaginaPreviaNoPermitida('Sin página previa')

        for pagina in self.paginas_permitidas:
            if pagina in pagina_anterior or pagina == "*":
                return super().dispatch(request, *args, **kwargs)

        raise PaginaPreviaNoPermitida(pagina_anterior)


@dataclass
class MigaNavegacion:
    url: str
    nombre: str
    activa: bool = True

    def __eq__(self, other):
        return self.url == other.url

    def serializar(self) -> dict:
        return asdict(self)

    @staticmethod
    def deserializar(diccionario: dict) -> 'MigaNavegacion':
        return MigaNavegacion(**diccionario)

    def __str__(self):
        return f'{self.nombre}=>({self.url})'

    def __repr__(self):
        return self.__str__()


class MigaDePanMixin:
    """
    Mixin que agrega migas de pan como ayuda de navegación.
    """
    _limite_migas_activas: int = 3
    _migas: list[MigaNavegacion] = field(default_factory=list)
    home = "/"
    nombre_esta_miga = 'Esta página'
    es_home = False
    mostrar_migas = None

    def agregar_miga(self, miga: MigaNavegacion, request) -> None:
        desde_sesion = request.session.get('migas', [])
        self._migas = [MigaNavegacion.deserializar(miga) for miga in desde_sesion]

        if not self.es_home:
            self.recrear_migas()

            if miga.url not in [m.url for m in self._migas]:
                self._migas.append(miga)

            self.evaluar_migas_activas(request)
            request.session['migas'] = [m.serializar() for m in self._migas]
            return

        self.limpiar_migas(request)

    def recrear_migas(self):
        if not self.home in [m.url for m in self._migas]:
            self._migas = [MigaNavegacion(url=self.home, nombre="Inicio")] + self._migas[-self._limite_migas_activas:]
        else:
            self._migas = self._migas[-self._limite_migas_activas:]

            if not self.home in [m.url for m in self._migas]:
                self._migas = [MigaNavegacion(url=self.home, nombre="Inicio")] + self._migas[-self._limite_migas_activas:]

    def evaluar_migas_activas(self, request):
        for miga in self._migas:
            miga.activa = miga.url != request.path

    def get_home(self) -> str:
        return self.home

    def get_nombre_esta_miga(self) -> str:
        return self.nombre_esta_miga

    def get_mostrar_migas(self) -> bool:
        if self.mostrar_migas is None:
            self.mostrar_migas = len(self._migas) > 1 and not self.es_home
        return self.mostrar_migas

    def limpiar_migas(self, request) -> None:
        self._migas = []
        request.session['migas'] = []

    def dispatch(self, request, *args, **kwargs):
        self.agregar_miga(
            MigaNavegacion(
                url=request.path,
                nombre=self.get_nombre_esta_miga(),
                activa=False
            ),
            request
        )
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['migas'] = self._migas
        context['mostrar_migas'] = self.get_mostrar_migas()
        return context
