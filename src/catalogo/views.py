
from django.http import HttpResponse
from django.views.generic import TemplateView, View, DetailView
from inventario.models import Producto

from catalogo.carrito.models import Carrito, EntradaCarrito



# Create your views here.
class Home(TemplateView):
    template_name= "web/index.html"

class VerCarritoView(TemplateView):
    template_name = 'web/carrito.html'

class ActualizarCarritoView(View):
    def post(self, request):
        carrito: Carrito = Carrito.deserializar(request.session['carrito'])
        data = request.POST
        cantidad = int(data['cantidad'])
        pk = int(data['pk'])

        producto: EntradaCarrito = carrito.obtener_producto(pk)
        cantidad_final = producto.cantidad - cantidad

        if cantidad_final < 0:
            carrito.aumentar_cantidad_producto(pk, abs(cantidad_final))
        elif cantidad_final > 0:
            carrito.disminuir_cantidad_producto(pk, abs(cantidad_final))

        carrito.guardar(request.session)
        return HttpResponse(carrito)

class AgregarProductoCarritoView(View):
    def post(self, request):
        carrito: Carrito = Carrito.deserializar(request.session['carrito'])
        data = request.POST
        pk = int(data['pk'])
        producto = EntradaCarrito(1, pk)
        carrito.agregar_producto(producto)
        carrito.guardar(request.session)
        return HttpResponse(carrito)

class DetalleProducto(DetailView):
    template_name= "web/detalle_pro.html"
    model= Producto

