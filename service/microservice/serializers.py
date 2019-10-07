from .models import Factura

from rest_framework import serializers

class FacturaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Factura
		fields = ('id',  'pedido_id', 'costo_total', 'impuesto_IVA')