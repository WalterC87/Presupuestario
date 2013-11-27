# -*- encoding: utf-8 -*-
from django.db import models
from bases.models import PlanDeCuentas, Proveedores
from django.contrib.auth.models import User 

# Create your models here.

class Reserva(models.Model):
	cuenta = models.ForeignKey('bases.PlanDeCuentas', blank=False,  null=False, verbose_name='Cuenta')
	monto = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Importe')
	concepto = models.CharField(max_length=200, verbose_name='Concepto Reserva')
	exp_nro = models.CharField(max_length=15, blank=False, null=False, verbose_name='Exp N°')
	proveedor = models.ForeignKey('bases.Proveedores', blank=False, null=False, verbose_name='Proveedor')
	fecha = models.DateField()
	usuario = models.ForeignKey(User)