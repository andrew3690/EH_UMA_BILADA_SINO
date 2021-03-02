from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic import TemplateView
#from Pedidos.models import Rodizio

class Listing(LoginRequiredMixin,TemplateView):
    template_name = 'management/Pedidos/litsting.html'

class A_la_carte_view(LoginRequiredMixin,TemplateView):
    template_name = 'management/Pedidos/A_la_carte/a_la_carte_orders.html'

class Rodizio_view(LoginRequiredMixin,TemplateView):
    template_name = 'management/Pedidos/Rodizio/rodizio_orders.html'

class Delivery_view(LoginRequiredMixin,TemplateView):
    template_name = 'management/Pedidos/Rodizio/delivery_orders.html'