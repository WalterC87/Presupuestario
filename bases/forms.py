from django import forms 
from django.forms import ModelForm
from .models import Proveedores, PlanDeCuentas

class ProveedoresForm(ModelForm):
	class Meta:
		model = Proveedores
		#excluyo los campos que no quiero mostrar en el form con exclude
		#exclude = ("votos,usuario")


class PlanDeCuentasForm(ModelForm):
	class Meta:
		model = PlanDeCuentas