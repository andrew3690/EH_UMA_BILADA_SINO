from django import forms
from .models import Funcionario, Objeto, Veiculo, Entrega

class RegisterFuncionarioForm(forms.ModelForm):
	class Meta:
		model = Funcionario
		fields = "__all__"

class RegisterObjetoForm(forms.ModelForm):
	class Meta:
		model = Objeto
		fields = "__all__"

class RegisterVeiculoForm(forms.ModelForm):
	class Meta:
		model = Veiculo
		fields = "__all__"

class RegisterEntregaForm(forms.ModelForm):
	class Meta:
		model = Entrega
		fields = "__all__"
