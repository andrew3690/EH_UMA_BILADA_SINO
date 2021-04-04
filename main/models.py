from django.db import models
from django.contrib.auth.models import User
import time
from datetime import timedelta
import datetime as dt
from django.utils.timezone import utc

REQUEST_TYPES = (
	('Pregos','pregos'),
	('Canos de PVC','canos de pvc'),
	('Fios de Cobre','fios de cobre'),
	('Tabuas de Madeira','tabuas de madeira'),
	('Massa de Revestimento','massa'),
	('Cimento','cimento'),
	('Tijolos','tijolos')
)

DELIVERY_TYPES = (
	('MEP','Maquinario Extremamente Pesado'),
	('MP','Maqunario Pesado'),
	('NN','Nao Necessita')
)

ROLE_TYPES = (
	('CA','Carregador'),
	('ODMD','Operador de Maquina'),
	('MC', 'Motorista de Caminhao')
)

STATES_CHOICES = (
	('AC', 'Acre'),
	('AL', 'Alagoas'),
	('AP', 'Amapá'),
	('AM', 'Amazonas'),
	('BA', 'Bahia'),
	('CE', 'Ceará'),
	('DF', 'Distrito Federal'),
	('ES', 'Espírito Santo'),
	('GO', 'Goiás'),
	('MA', 'Maranhão'),
	('MT', 'Mato Grosso'),
	('MS', 'Mato Grosso do Sul'),
	('MG', 'Minas Gerais'),
	('PA', 'Pará'),
	('PB', 'Paraíba'),
	('PR', 'Paraná'),
	('PE', 'Pernambuco'),
	('PI', 'Piauí'),
	('RJ', 'Rio de Janeiro'),
	('RN', 'Rio Grande do Norte'),
	('RS', 'Rio Grande do Sul'),
	('RO', 'Rondônia'),
	('RR', 'Roraima'),
	('SC', 'Santa Catarina'),
	('SP', 'São Paulo'),
	('SE', 'Sergipe'),
	('TO', 'Tocantins'),
)

class Funcionario(models.Model):
	nome = models.CharField(
		max_length= 30,
		default = "Arnaldao Sangue Bom"
	)

	funcao = models.CharField(
		max_length= 50,
		default = "nenhuma",
		choices = ROLE_TYPES
	)

	em_uso = models.BooleanField(
		default = False
	)

	def __str__(self):
		return "%s, %s"%(self.nome, self.funcao)

	class Meta:
		verbose_name_plural = "Funcionarios"
	
class Objeto(models.Model):
	objeto = models.CharField(
		max_length = 25,
		default= "esperando",
		choices = REQUEST_TYPES
	)

	espaco = models.IntegerField(
		null = True
	)

	quantidade = models.IntegerField(
		null = True
	)

	peso = models.IntegerField(
		default = 000
	)

	def __str__(self):
		return "%d %s"%(self.quantidade, self.objeto)

	def get_espaco_total(self):
		return (self.espaco * self.quantidade)
	
	def calcula_peso(self):
		peso_final = self.peso * self.quantidade
		return peso_final
	
	class Meta:
		verbose_name_plural = "Objetos"

class Veiculo(models.Model):
	placa = models.CharField(
		max_length = 40,
		default = ""
	)

	espaco_usado = models.IntegerField(
		default = 0
	)

	capacidade = models.IntegerField(
		default = 0000
	)

	em_uso = models.BooleanField(
		default = False
	)

	produtos = models.ManyToManyField(
		Objeto
	)

	def retorna_carga(self):
		bol = False
		cap = self.capacidade
		if cap <= 2500:
			bol = True
			return "Veiculo de baixa capacidade de carga"
		elif cap < 2500 and cap <= 5000:
			bol = True
			return "Veiculo de média capacidade de carga"
		elif cap > 5000:
			bol = True
			return "Veiculo de alta capacidade de carga"

	def peso_total(self):
		lista = []
		for produto in self.produtos.all():
			lista.append(produto.calcula_peso())
		peso = sum(lista)
		return peso
	'''
	def carga_total(self):
		comp = self.retorna_carga()
		while(comp != True):
			return "este veiculo não suporta esta quantidade de carga"
		return self.peso_total()	
	'''
	def __str__(self):
		return "placa: %s, capacidade: %s" %(self.placa, self.capacidade)

	class Meta:
		verbose_name_plural = "Veiculos"

class Entrega(models.Model):
	descarga = models.CharField(
		max_length = 40,
		default= 'esperando',
		choices = DELIVERY_TYPES
	)

	address = models.CharField(
		max_length = 200,
		default = "endereço"
	)

	address_complement = models.CharField(
		max_length = 250,
		blank = True,
		null = True
	)

	city = models.CharField(
		max_length = 200,
		default = "city"
	)

	states = models.CharField(
		max_length = 200,
		choices = STATES_CHOICES,
		default="states"
	)

	country = models.CharField(
		max_length = 200,
		default="country"
	)

	user = models.ForeignKey(
		User,
		blank = True,
		null = True,
		on_delete = models.PROTECT
	)

	veiculo = models.ForeignKey(
		Veiculo,
		on_delete = models.CASCADE,
		null = True
	)

	produtos = models.ManyToManyField(
		Objeto
	)

	funcionarios = models.ManyToManyField(
		Funcionario
	)

	time = models.DateTimeField(
		null = True,
		blank = True
	)

	def get_time_diff(self):
		if (self.time):
			t = dt.datetime.now()
			return self.time.replace(tzinfo=None) - t
		return "ainda nao enviado"

	
	class Meta:
		verbose_name_plural = "Entregas"


	def __str__(self):
		return "%s"%(self.address)

class Loja(models.Model):
	identificacao = models.CharField(
		max_length = 200,
		default = "loja"
	)

	city = models.CharField(
		max_length = 200,
		default = "city"
	)

	states = models.CharField(
		max_length = 200,
		choices = STATES_CHOICES,
		default="states"
	)

	veiculos = models.ManyToManyField(
		Veiculo
	)

	funcionarios = models.ManyToManyField(
		Funcionario
	)

	entregas = models.ManyToManyField(
		Entrega
	)

	def get_veiculo_disponivel(self, espaco):
		for veiculo in self.veiculos.all():
			print(veiculo.em_uso, veiculo.capacidade, espaco)
			if ((not veiculo.em_uso) and (veiculo.capacidade - veiculo.espaco_usado >= espaco)):
				return veiculo
		return None
	
	def get_funcionarios_disponiveis(self):
		for funcionario in self.funcionarios.all():
			print(funcionario)
			if (not funcionario.em_uso):
				return [funcionario]
		return None

	def __str__(self):
		return ("%s" % (self.identificacao))

