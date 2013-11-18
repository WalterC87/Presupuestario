# -*- encoding: utf-8 -*-

from django.db import models

class Presupuestos(models.Model):
	anio = models.DateField()
	ordenanza = models.CharField(max_length=50)
	thumb = models.ImageField(upload_to='media/')
	monto = models.DecimalField(max_digits=15, decimal_places=2)

	def __unicode__(self):
		return "N° Ord: %s - Año: %s" % (self.ordenanza, self.anio)

class PlanDeCuentas(models.Model):
	nombrecuenta = models.CharField(max_length=180)
	cuentapadre = models.ForeignKey('self', blank=True,  null=True)
	monto = models.DecimalField(max_digits=15, decimal_places=2)
	presupuesto = models.ForeignKey(Presupuestos)
	thumb = models.ImageField(upload_to='media/')

	def __unicode__(self):
		return " %s " % (self.nombrecuenta)


class Proveedores(models.Model):
	razonsocial = models.CharField(max_length=140, null=False, blank=False)
	cuit = models.CharField(max_length=11, null=False, blank=False)
	direccion = models.CharField(max_length=140, null=False, blank=False )
	tel_fijo = models.CharField(max_length=15)
	tel_cel = models.CharField(max_length=15)
	email = models.EmailField(max_length=254)
	www = models.URLField()

	def __unicode__(self):
		return " %s - CUIT: %s " % (self.razonsocial, self.cuit)