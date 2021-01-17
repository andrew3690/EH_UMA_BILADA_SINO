from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Address
from .forms import AddressForm

def index(request):
    return render(request,'templates/index.html')

def login(request = HttpResponse):
    if request.method == 'GET':
        return render(request,'django_intermediario/login.html')
    
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username = username,password=password)

    if user:
        django_login(request,user)
        #return HttpResponseRedirect('/home/') Utilize from django.hhtp import HtttpResponseRedirect 
        return render(request,'django_intermediario/home.html')
    else:
        message = 'Credenciais invalidas'
        return render(request,'django_intermediario/login.html',{'message':message})

@ login_required(login_url = '/login/')
def home(request):
    return render(request,'django_intermediario/home.html')

@ login_required(login_url = '/login/')
def logout(request):
    logout = django_logout(request)
    return render(request,'django_intermediario/login.html',{'logout':logout})

@ login_required(login_url= '/login/')
def address_list(request):
    addresses = Address.objects.all()
    return render(request,'django_intermediario/list.html',{'addresses':addresses})

@ login_required(login_url='/login/')
def create(request):
    form_submitted = False
    if request.method == "GET":
        form = AddressForm()
    else:
        form_submitted = True
        form = AddressForm(request.POST)
        if form.is_valid():
            address =   form.save(commit= False)
            address.user = request.user
            address.save()
            '''
            Address.objects.create(
                    address = form.cleaned_data['address'],
                    address_complement = form.cleaned_data['address_complement'],
                    city = form.cleaned_data['city'],
                    states = form.cleaned_data['states'],
                    country = form.cleaned_data['country'],
                    user = request.user
            )
            '''
            return redirect(reverse('management:address_list'))
    
    return render(request,'django_intermediario/create.html',{'form':form,'form_submitted':form_submitted})

@ login_required(login_url='/login/')
def update(request,id):
    form_submitted = False
    address = Address.objects.get(id = id)
    if request.method == 'GET':
        #form = AddressForm(address.__dict__)
        form = AddressForm(instance=address)
    else:
        form_submitted = True
        form = AddressForm(request.POST,instance=address)
        if form.is_valid():
            form.save()
            '''
            address.address = request.POST.get('address')
            address.address_complement = request.POST.get('address_complement')
            address.city = request.POST.get('city')
            address.states = request.POST.get('states')
            address.country = request.POST.get('country')
            address.save()
            '''
            return redirect(reverse('management:address_list'))
    
    return render(request,'django_intermediario/update.html',{'address':address,'form':form, 'form_submitted':form_submitted})
        
@ login_required(login_url='/login/')
def destroy(request,id):
    address = Address.objects.get(id = id)
    if request.method == 'GET':
        #form = AddressForm(address.__dict__)
        form = AddressForm(instance=address)
    else:
        address.delete()
        return redirect(reverse('management:address_list'))
    return render(request,'django_intermediario/destroy.html',{'address':address,'form':form})
        