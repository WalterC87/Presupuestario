from django import forms 
from django.forms import ModelForm
from .models import Reserva, OrdenPago

class ReservaForm(ModelForm):
	class Meta:
		model = Reserva
		#excluyo los campos que no quiero mostrar en el form con exclude
		exclude = ("usuario")

class OrdenPagoForm(ModelForm):
	class Meta:
		model = OrdenPago
		exclude = ("usuario")
			