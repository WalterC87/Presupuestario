from django.db import models

class Presupuestos(models.Model):
	anio = models.DateField()
	ordenanza = models.CharField(max_length=50)
	thumb = models.ImageField(upload_to='/static/')
	monto = models.FloatField()

class PlanDeCuentas(models.Model):
	nombrecuenta = models.CharField(max_length=180)
	cuentapadre = models.ForeignKey('self')
	monto = models.FloatField()
	presupuesto = models.ForeignKey(Presupuestos)
	thumb = models.ImageField(upload_to = '')

class Proveedores(models.Model)
	razonsocial = models.CharField(max_length=140, null=False, blank=False)
	cuit = models.CharField(max_length=11, null=False, blank=False)
	direccion = models.CharField(max_length=140, null=False, blank=False )
	tel_fijo = models.CharField(max_length=15)
	tel_cel = models.CharField(max_length=15)
	email = models.EmailField(max_length=254)
	www = models.URLField()