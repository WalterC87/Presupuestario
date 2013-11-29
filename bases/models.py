# -*- encoding: utf-8 -*-
from django.db import models
from django.core.validators import RegexValidator

class Presupuestos(models.Model):
	anio = models.CharField(max_length=4, verbose_name='Año')
	ordenanza = models.CharField(max_length=50, verbose_name='Nro Ordenanza')
	thumb = models.ImageField(upload_to='media/', verbose_name='Img.')
	monto = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Importe Total')

	def __unicode__(self):
		return "Ord: %s - Anio: %s" % (self.ordenanza, self.anio)

class PlanDeCuentas(models.Model):
	nombrecuenta = models.CharField(max_length=180, verbose_name='Nombre de Cuenta')
	cuentapadre = models.ForeignKey('self', blank=True,  null=True, verbose_name='Cuenta Padre')
	monto = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Importe Total')
	presupuesto = models.ForeignKey(Presupuestos, verbose_name='Presupuesto')
	codigo = models.CharField(max_length=40, blank=False, null=False, verbose_name='Cod. Cuenta')
	thumb = models.ImageField(upload_to='media/', verbose_name='Img.')
	#monto_reservado = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Importe Total')
	#monto_imputado = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Importe Total')

	def __unicode__(self):
		return " %s : %s " % (self.codigo, self.nombrecuenta)


class Proveedores(models.Model):
	razonsocial = models.CharField(max_length=140, null=False, blank=False, verbose_name='R. Social')
	cuit = models.CharField(max_length=11,
			validators = [
                RegexValidator(
                                '^[0-9]*$',
                                 'Solo puede ingresar dígitos',
                )
            ],  null=False, blank=False, verbose_name='CUIT')
	direccion = models.CharField(max_length=140, null=False, blank=False, verbose_name='Domicilio')
	tel_fijo = models.CharField(max_length=15, verbose_name='Tel.')
	tel_cel = models.CharField(max_length=15, verbose_name='Cel.')
	email = models.EmailField(max_length=254, verbose_name='Email')
	www = models.URLField(verbose_name='Sitio Web')
	dni = models.CharField(
                max_length = 8,
                validators = [
                        RegexValidator(
                                '^[0-9]*$',
                                 'Solo puede ingresar dígitos',
                        )
                ], 
                blank = False)


	def __unicode__(self):
		return " %s - CUIT: %s " % (self.razonsocial, self.cuit)