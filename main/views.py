from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView,View,RedirectView,ListView, DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from .models import Entrega,Funcionario,Objeto,Veiculo

'''
class FormSubmittedInContextMixin:
	def form_invalid(self,form):
		return self.render_to_reponse(self.get_contenxt_data(form= form, form_sumitted = True))
'''

class LoginView(TemplateView):
	template_name = 'home/auth/login.html'

	def post(self,request,*agrs,**kwargs):
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username = username,password=password)

		if user:
			django_login(request,user)
			return render(request,'home/home.html')
		else:
			message = 'Credenciais invalidas'
			return render(request,self.template_name,{'message':message})

class HomeView(LoginRequiredMixin,TemplateView):
	template_name = 'home/home.html'

class LogoutRedirectView(LoginRequiredMixin,RedirectView):
	url = '/login/'

	def get(self, request, *args, **kwargs):
		django_logout(request)
		return super().get(request, *args, **kwargs)

class EntregaDetailView(LoginRequiredMixin,DetailView):
	model = Entrega
	template_name = 'cliente/entrega_detail.html'

	def get_queryset(self,*args,**kwargs):
		queryset = Entrega.objects.filter(user = self.request.user)
			
		for o in queryset:
			o.enviar()
		return queryset
	
class EntregaListView(LoginRequiredMixin,ListView):
	model = Entrega
	template_name = 'cliente/entregas_list.html'

	## separaçao de objetos de cada usuario
	def get_queryset(self,*args,**kwargs):
		queryset = Entrega.objects.filter(user = self.request.user)
			
		for o in queryset:
			o.enviar()
		return queryset
