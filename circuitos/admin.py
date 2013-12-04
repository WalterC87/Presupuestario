# -*- encoding: utf-8 -*-
from django.contrib import admin
from models import *

class ReservaAdmin(admin.ModelAdmin):
	list_display = ('cuenta','monto','nro_asignacion',)	

class OrdenPagoAdmin(admin.ModelAdmin):
	list_display = ('compromiso','fec_emision','monto','cuenta',)	

admin.site.register(Reserva, ReservaAdmin)
admin.site.register(OrdenPago,OrdenPagoAdmin)
