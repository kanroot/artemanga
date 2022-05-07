from django.http import HttpResponse
from django.views.generic import TemplateView, View, ListView, DetailView

from catalogo.carrito.models import Carrito, EntradaCarrito
from inventario.models import Producto, Genero, Editorial


class Home(TemplateView):
    template_name= "web/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['randoms'] = Producto.objects.order_by('?')[:5]
        return context


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


class ProductosPorCategoriaView(ListView):
    template_name = 'web/catalogo_filtrado.html'
    context_object_name = 'productos'
    extra_context = {}

    def get_queryset(self):
        genero = Genero.objects.get(id=self.kwargs['id'])
        self.extra_context['filtro_desc'] = 'categoría'
        self.extra_context['filtro'] = genero
        return Producto.objects.filter(esta_publicado=True).filter(genero=genero)


class ProductosPorEditorialView(ListView):
    template_name = 'web/catalogo_filtrado.html'
    extra_context = {'filtro_desc': 'editorial'}
    context_object_name = 'productos'

    def get_queryset(self):
        editorial = Editorial.objects.get(id=self.kwargs['id'])
        self.extra_context['filtro_desc'] = 'editorial'
        self.extra_context['filtro'] = editorial
        return Producto.objects.filter(esta_publicado=True).filter(editorial=editorial)

class DetalleProducto(DetailView):
    template_name= "web/detalle_pro.html"
    model= Producto

