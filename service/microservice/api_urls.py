#from django.conf.urls import path
from django.urls import path,include
from microservice.views import *

from rest_framework import routers

router = routers.DefaultRouter()
router.register('factura', GetFactura)

urlpatterns =[
	path('factura/',include(router.urls)),
]