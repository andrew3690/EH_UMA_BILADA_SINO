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

STATUS_TYPES = (
	('Aguardando Pedido','pedido aguardando'),
	('Entrega em Andamento','entrega em andamento'),
	('Entregue','entregue')
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

	def __str__(self):
		return "%s, %s"%(self.nome, self.funcao)

	class Meta:
		verbose_name_plural = "Funcionarios"

class Veiculo(models.Model):
	placa = models.CharField(
		max_length = 40,
		default = ""
	)

	def __str__(self):
		return "%s" %(self.placa)

	class Meta:
		verbose_name_plural = "Veiculos"
	
class Objeto(models.Model):
	objetos = models.CharField(
		max_length = 25,
		default= "esperando",
		choices = REQUEST_TYPES
	)

	def __str__(self):
		return "%s"%(self.objetos)
	
	class Meta:
		verbose_name_plural = "Objetos"

class Entrega(models.Model):
	status = models.CharField(
		max_length= 40,
		default= 'esperando',
		choices = STATUS_TYPES
	)
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
			print(type(self), type(self.time))
			t = dt.datetime.now()
			return self.time.replace(tzinfo=None) - t
		return "ainda nao enviado"
	'''
	def timeLeft(self):
		t = time.time()
		perido = self.tempo - t 
		return perido

	#time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(ts))

	'''
	'''
		intervalo_tempo = 10
		t = time.time()
		return t - self.time
		#return time.strftime("%H:%M", timedelta(self.time - t)
	'''
	
	class Meta:
		verbose_name_plural = "Entregas"


	def __str__(self):
		return "%s"%(self.address)

