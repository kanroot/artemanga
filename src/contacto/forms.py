from django import forms
from .models import Mensaje, Ticket
from ckeditor.widgets import CKEditorWidget
from .enums.tipo_ticket import TIPO_TICKET_CHOICES
from venta.models import Venta

class CrearMensajeForm(forms.Form):
    texto = forms.CharField(label=False, widget=CKEditorWidget())

    class Meta:
        fields = ['texto']
        model = Mensaje


class CrearTicketForm(forms.Form):
    titulo = forms.CharField(max_length=100, label='Breve descripción de este ticket')
    tipo = forms.ChoiceField(choices=TIPO_TICKET_CHOICES, label='Tipo de ticket')
    venta = forms.ModelChoiceField(queryset=Venta.objects.none(), label='Venta asociada', required=False)

    class Meta:
        model = Ticket
        fields = ['titulo', 'tipo', 'venta']

    def __init__(self, *args, **kwargs):
        self.usuario = kwargs.pop('usuario')
        super().__init__(*args, **kwargs)
        self.fields['venta'].queryset = Venta.objects.filter(usuario=self.usuario)