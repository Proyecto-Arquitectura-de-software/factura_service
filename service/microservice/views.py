from django.shortcuts import render, get_object_or_404

from rest_framework import generics,viewsets
from .models import Factura 
from .serializers import FacturaSerializer
from .models import Factura

class GetFactura(viewsets.ModelViewSet):
	queryset = Factura.objects.all()
	serializer_class = FacturaSerializer