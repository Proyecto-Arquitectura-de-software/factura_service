from django.db import models


class Factura(models.Model):
	pedido_id = models.IntegerField()
	costo_total = models.IntegerField()
	impuesto_IVA = models.IntegerField()
	