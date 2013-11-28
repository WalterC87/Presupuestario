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
	fecha_afectacion = models.DateField(verbose_name='Fecha Afectación')
	nro_asignacion = models.CharField(max_length=15, blank=False, verbose_name='N° Asig.')
	usuario = models.ForeignKey(User)

	def __unicode__(self):
		return " %s : %s " % (self.cuenta, self.monto)


class OrdenPago(models.Model):
	compromiso = models.CharField(max_length=15,blank=False, null=False, verbose_name='Compromiso N°')
	fec_emision = models.DateField(verbose_name='Fecha Emisión')
	beneficiario = models.ForeignKey('bases.Proveedores', blank=False, null=False, verbose_name='Beneficiario')
	concepto = models.CharField(max_length=200, verbose_name='Concepto')
	monto = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Monto')
	exp_nrohcd = models.CharField(max_length=15, blank=True, null=True, verbose_name='Exp HCD N°')
	cuenta = models.ForeignKey('bases.PlanDeCuentas', blank=False,  null=False, verbose_name='Cuenta')
	#consultar por Asignacion, si pueden ser mas de una x reserva
	asignacion = models.CharField(max_length=15, blank=False, null=False, verbose_name='N° Asig.')	
	usuario = models.ForeignKey(User)

	def __unicode__(self):
		return " %s : %s " % (self.compromiso, self.monto)
	