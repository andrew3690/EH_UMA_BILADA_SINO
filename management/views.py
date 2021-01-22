from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Address
from .forms import AddressForm
from django.views.generic import TemplateView,View,RedirectView,ListView, DetailView, CreateView, DeleteView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin 
from api_temakin.settings import LOGIN_URL
from django.urls import reverse_lazy

class FormSubmittedInContextMixin:
    def form_invalid(self,form):
        return self.render_to_reponse(self.get_contenxt_data(form= form, form_sumitted = True))

class LoginView(TemplateView):
    template_name = 'management/auth/login.html'
    
    def post(self,request,*agrs,**kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username,password=password)

        if user:
            django_login(request,user)
            return render(request,'management/home.html')
        else:
            message = 'Credenciais invalidas'
            return render(request,self.template_name,{'message':message})

class HomeView(LoginRequiredMixin,TemplateView):
    template_name = 'management/home.html'


class LogoutRedirectView(LoginRequiredMixin,RedirectView):
    url = '/login/'

    def get(self, request, *args, **kwargs):
        django_logout(request)
        return super().get(request, *args, **kwargs)

class AddressDetailView(LoginRequiredMixin,DetailView):
    model = Address
    template_name = 'management/address/detail.html'


class AddressListView(ListView):
    model = Address
    template_name = 'management/address/list.html'

class AddressCreateView(LoginRequiredMixin,FormSubmittedInContextMixin,CreateView):
    model = Address
    form_class = AddressForm 
    template_name = 'management/address/create.html'
    success_url =  reverse_lazy(('management:address_list'))

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class AddressUpdateView(UpdateView, LoginRequiredMixin, FormSubmittedInContextMixin):
    model = Address
    form_class = AddressForm
    template_name = 'management/address/update.html'

class AddressDestroyView(LoginRequiredMixin,DeleteView):
    model = Address
    template_name = 'management/address/destroy.html'
    success_url =  reverse_lazy(('management:address_list'))


