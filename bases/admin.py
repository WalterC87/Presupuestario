from django.contrib import admin
from models import Presupuestos, PlanDeCuentas, Proveedores

class PresupuestosAdmin(admin.ModelAdmin):
	list_display = ('anio', 'monto', 'ordenanza',)
	# muestra los campos divididos por columnas en la grilla

class ProveedoresAdmin(admin.ModelAdmin):
	list_display = ('razonsocial','cuit','direccion','tel_fijo','email')	

class PlanDeCuentasAdmin(admin.ModelAdmin):
	list_display = ('nombrecuenta','cuentapadre','monto','presupuesto')	
	

admin.site.register(Presupuestos,PresupuestosAdmin)
admin.site.register(Proveedores,ProveedoresAdmin)
admin.site.register(PlanDeCuentas,PlanDeCuentasAdmin)
