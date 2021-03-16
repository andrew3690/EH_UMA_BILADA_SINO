from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView,View,RedirectView,ListView, DetailView
from django.views.generic.edit import FormView, CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User
import time
from datetime import timedelta
import datetime as dt

from .models import Entrega,Funcionario,Objeto,Veiculo
from .forms import RegisterFuncionarioForm, RegisterObjetoForm, RegisterVeiculoForm, RegisterEntregaForm


'''
class FormSubmittedInContextMixin:
	def form_invalid(self,form):
		return self.render_to_reponse(self.get_contenxt_data(form= form, form_sumitted = True))
'''
class HomeGerenciadorView(LoginRequiredMixin, ListView):
	template_name = "admin/home.html"
	model = Entrega

class CreateFuncionarioView(LoginRequiredMixin, FormView, CreateView):
	template_name = "admin/create_funcionario.html"
	form_class = RegisterFuncionarioForm
	def get_success_url(self):
		return reverse('main:gerenciador_funcionarios')

class CreateObjetoView(LoginRequiredMixin, FormView, CreateView):
	template_name = "admin/create_objeto.html"
	form_class = RegisterObjetoForm
	def get_success_url(self):
		return reverse('main:gerenciador_objetos')
		
class CreateVeiculoView(LoginRequiredMixin, FormView, CreateView):
	template_name = "admin/create_veiculo.html"
	form_class = RegisterVeiculoForm
	def get_success_url(self):
		return reverse('main:gerenciador_veiculos')

class CreateEntregaView(LoginRequiredMixin, FormView, CreateView):
	template_name = "admin/create_entrega.html"
	form_class = RegisterEntregaForm
	def get_success_url(self):
		return reverse('main:gerenciador_entregas')

class EntregaGerListView(LoginRequiredMixin, ListView):
	model = Entrega
	template_name = "admin/list_entregas.html"

class FuncionarioGerListView(LoginRequiredMixin, ListView):
	model = Funcionario
	template_name = "admin/list_funcionarios.html"

class ObjetoGerListView(LoginRequiredMixin, ListView):
	model = Objeto
	template_name = "admin/list_objetos.html"

class VeiculoGerListView(LoginRequiredMixin, ListView):
	model = Veiculo
	template_name = "admin/list_veiculos.html"

def EnviarEntrega(request, pk):
	o = Entrega.objects.filter(pk = pk).get()
	now = dt.datetime.now()
	#delta = dt.timedelta(hours = 2)
	o.time = now #+ delta
	o.save()
	print(o.time)
	return HttpResponseRedirect(reverse('main:gerenciador_entregas'))


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
	def get_queryset(self, *args, **kwargs):
		o = Entrega.objects.filter(pk = self.kwargs["pk"])
		return o

class EntregaDetailProdutosView(LoginRequiredMixin, ListView):
	model = Entrega
	template_name = "cliente/entrega_detail_produtos.html"
	def get_queryset(self, *args, **kwargs):
		o = Entrega.objects.filter(pk = self.kwargs["pk"])
		return o.get().produtos.all()

class EntregaDetailFuncionariosView(LoginRequiredMixin, ListView):
	model = Entrega
	template_name = "cliente/entrega_detail_funcionarios.html"
	def get_queryset(self, *args, **kwargs):
		o = Entrega.objects.filter(pk = self.kwargs["pk"])
		return o.get().funcionarios.all()

class EntregaListView(LoginRequiredMixin,ListView):
	model = Entrega
	template_name = 'cliente/entregas_list.html'

	## separaçao de objetos de cada usuario
	def get_queryset(self,*args,**kwargs):
		queryset = Entrega.objects.filter(user = self.request.user)
		return queryset
