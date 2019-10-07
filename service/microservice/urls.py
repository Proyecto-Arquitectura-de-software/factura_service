from django.conf.urls import path
from microservice.views import *


urlpatterns = [
	path('factura/$', factura)
]