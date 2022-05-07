from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, FormView, TemplateView

from artemangaweb.mixins import VistaRestringidaMixin, TituloPaginaMixin, ImpedirSinRedireccionMixin
from catalogo.carrito.models import Carrito
from inventario.models import Producto
from .forms import CrearDireccionForm, ElegirDireccionForm
from .models import Direccion, ComprobanteTemporal, VentaProducto, Venta, Despacho
from sistema.models import RegistroError


class ConfirmarCompraView(ImpedirSinRedireccionMixin, VistaRestringidaMixin, View):
    usuarios_permitidos = VistaRestringidaMixin.todos_los_usuarios
    paginas_permitidas = ['ver-carrito']
    permission_denied_message = '¡Debe iniciar sesión o registrarse para realizar una compra!'

    def get(self, request):
        return HttpResponseRedirect(reverse('ver-carrito'))

    def post(self, request):
        archivo = request.FILES['adjuntoTransferencia']
        # Guardemos el comprobante mientras tanto, no hay forma de pasarlo a otras vistas
        comprobante_temporal = ComprobanteTemporal(usuario=request.user)
        comprobante_temporal.comprobante.save(archivo.name, archivo)
        comprobante_temporal.save()

        direcciones = Direccion.objects.filter(usuario=request.user)

        if not direcciones:
            messages.warning(request, '¡Es necesario crear una dirección para mandar sus productos!')
            return HttpResponseRedirect(reverse('crear-direccion') + '?next=' + request.path)

        return HttpResponseRedirect(reverse('elegir-direccion'))

class CrearDireccionView(VistaRestringidaMixin, TituloPaginaMixin, CreateView):
    titulo_pagina = 'Crear dirección de envío'
    usuarios_permitidos = VistaRestringidaMixin.todos_los_usuarios
    permission_denied_message = '¡Debe iniciar sesión o registrarse para agregar una dirección a su usuario!'
    model = Direccion
    form_class = CrearDireccionForm
    template_name = 'web/generico_form.html'
    success_url = reverse_lazy('elegir-direccion')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['initial']['usuario'] = self.request.user.pk
        return kwargs

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class ElegirDireccionView(ImpedirSinRedireccionMixin, VistaRestringidaMixin, TituloPaginaMixin, FormView):
    usuarios_permitidos = VistaRestringidaMixin.todos_los_usuarios
    paginas_permitidas = ['crear-direccion', 'confirmar-compra', 'ver-carrito', 'elegir-direccion']
    titulo_pagina = 'Elegir dirección de envío'
    template_name = 'web/elegir_direccion.html'
    form_class = ElegirDireccionForm
    success_url = reverse_lazy('finalizar-compra')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['usuario'] = self.request.user
        return kwargs

    def get_success_url(self):
        url = super().get_success_url() + f'?direccion={self.request.POST.get("direccion", )}'
        return url

class FinalizarCompraView(ImpedirSinRedireccionMixin, VistaRestringidaMixin, TemplateView):
    usuarios_permitidos = VistaRestringidaMixin.todos_los_usuarios
    paginas_permitidas = ['elegir-direccion']
    template_name = 'web/finalizar_compra.html'
    extra_context = {}

    def get(self, request, *args, **kwargs):
        carrito: Carrito = Carrito.deserializar(request.session['carrito'])

        try:
            direccion = Direccion.objects.get(pk=request.GET.get('direccion', ))
            temp = ComprobanteTemporal.objects.filter(usuario=request.user).latest('fecha_creacion')
            despacho = Despacho(direccion=direccion)
            despacho.save()
            venta = Venta(despacho=despacho, total=carrito.total)
            venta.imagen_deposito.save(temp.comprobante.name, temp.comprobante.file)

            for entrada in carrito.productos:
                venta_producto = VentaProducto(
                    venta=venta,
                    cantidad=entrada.cantidad,
                    producto=Producto.objects.get(pk=entrada.pk),
                )
                venta_producto.save()
            venta.save()
        except Exception as e:
            error = RegistroError(
                error=str(e),
                descripcion=f'Error al finalizar la compra del usuario {request.user.username}',
                data=carrito.serializar(),
                usuario=request.user,
                pagina=self.request.path
            )
            error.save()
            self.extra_context['error'] = error.id
        else:
            carrito.vaciar()
            carrito.guardar(request.session)
            temp.delete()
            self.extra_context['id_venta'] = venta.pk

        return super().get(request, **kwargs)
