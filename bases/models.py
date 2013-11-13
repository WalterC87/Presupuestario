from django.db import models

class Presupuestos(models.Model):
	anio = models.DateField()
	ordenanza = models.CharField(max_length=50)
	thumb = models.ImageField(upload_to='/static/')
	monto = models.FloatField(max_digits=15, decimal_places=2, null=False)

class PlanDeCuentas(models.Model):
	nombrecuenta = models.CharField(max_length=180)
	cuentapadre = models.IntegerField(null=True)
	monto = models.FloatField(max_digits=15, decimal_places=2, null=False)
	presupuesto = models.ForeignKey(Presupuesto)
	thumb = models.ImageField(upload_to='/static/')

class Proveedores(models.Model):
	razonsocial = models.CharField(max_length=140 null=False blank=False)
	cuit = models.CharField(max_length=11 null=False blank=False)
	direccion = models.CharField(max_length=140 null=False blank=False)
	tel_fijo = models.CharField(max_length=15)
	tel_cel = models.CharField(max_length=15)
	email = models.EmailField(max_length=254)
	www = models.URLField()