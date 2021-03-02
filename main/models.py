from django.db import models
from django.contrib.auth.models import User
import time
from datetime import timedelta


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
	('PA','pedido aguardando'),
	('EA','entrega em andamento'),
	('E','entregue')
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

class Entrega(models.Model):
	numero = models.CharField(
		max_length = 20,
		default = "000-000"
	)
	objetos = models.CharField(
		max_length = 25,
		default= "esperando",
		choices = REQUEST_TYPES
	)
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

	CEP = models.CharField(
		max_length= 10,
		default= "00.000-000"
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

	matricula = models.CharField(
		max_length= 30,
		default = "000"
	)

	nome = models.CharField(
		max_length= 30,
		default = "Arnaldao Sangue Bom"
	)

	funçao = models.CharField(
		max_length= 50,
		default = "nenhuma",
		choices = ROLE_TYPES
	)

	user = models.ForeignKey(
		User,
		blank = True,
		null = True,
		on_delete = models.PROTECT
	)

	#time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(ts))

	#tempo = models.TimeField(auto_now_add=True)
	def enviar(self):
		self.time = time.time()

	def timeLeft(self):
		intervalo_tempo = 10
		t = time.time()
		return t - self.time
		#return time.strftime("%H:%M", timedelta(self.time - t)

	class Meta:
		verbose_name_plural = "Entregas"


	def __str__(self):
		return "%s, %s"%(self.numero,self.status)
