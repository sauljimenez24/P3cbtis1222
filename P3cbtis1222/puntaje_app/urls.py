from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("contactos/", views.contactos, name="contactos"),
    path("empleado/", views.empleado, name="empleado"),
    path("carros/", views.carros, name="carros"),
    path("motos/", views.motos, name="motos"),
    path("cliente/", views.cliente, name="cliente"),
    path("provedores/", views.provedores, name="provedores"),



    


]

