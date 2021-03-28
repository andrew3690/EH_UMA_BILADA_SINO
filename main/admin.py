from django.contrib import admin
from .models import Entrega,Funcionario,Veiculo,Objeto,Loja

# Register your models here.
admin.site.register(Entrega)
admin.site.register(Funcionario)
admin.site.register(Objeto)
admin.site.register(Veiculo)
admin.site.register(Loja)
