from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.db import models

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

class Address(models.Model):
    address = models.CharField(max_length = 200,default = "address")
    address_complement = models.CharField(max_length = 250,blank = True,null = True)
    city = models.CharField(max_length = 200,default = "city")
    states = models.CharField(max_length = 200,choices = STATES_CHOICES,default="states")
    country = models.CharField(max_length = 200,default="country")
    user = models.ForeignKey(User,on_delete = models.PROTECT)

    class Meta:
        verbose_name_plural = 'Adresses'
    
    @property
    def address_complement_normalaized(self):
        return '' if self.address_complement is None else self.address_complement

    def get_absolute_url(self):
        return reverse('management:address_detail', kwargs ={'pk':self.pk})
    
    def __str__(self):
        return "%s, %s ,%s"%(self.address,self.city,self.country)
