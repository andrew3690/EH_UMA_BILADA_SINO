from django import forms
from .models import Funcionario, Objeto, Veiculo, Entrega, Loja

class RegisterFuncionarioForm(forms.ModelForm):
	class Meta:
		model = Funcionario
		exclude = ["em_uso"]

class RegisterObjetoForm(forms.ModelForm):
	class Meta:
		model = Objeto
		fields = "__all__"

class RegisterVeiculoForm(forms.ModelForm):
	class Meta:
		model = Veiculo
		exclude = ["em_uso", "espaco_usado"]

class RegisterEntregaForm(forms.ModelForm):
	class Meta:
		model = Entrega
		#fields = "__all__"
		exclude = ['time', 'veiculo', 'funcionarios']

class RegisterLojaForm(forms.ModelForm):
	class Meta:
		model = Loja
		exclude = ["entregas"]
		
