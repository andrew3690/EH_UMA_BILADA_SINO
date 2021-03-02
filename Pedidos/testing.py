'''

class Bebidas(models.Model):
    name = models.CharField(max_length=200,default="Agua")
    desc = models.CharField(max_length=200,default='some description')
    preço_bebidas = models.DecimalField(decimal_places=2,max_digits=3,default=0.00)

class A_la_carte(models.Model):
    pratos = models.ForeignKey(
        Pratos,
        on_delete=models.CASCADE,
        default= 1
    )
    
    bebidas = models.ForeignKey(
        Bebidas,
        on_delete=models.CASCADE,
        default= 1
    )
    
    extras = models.ForeignKey(
        Extras,
        on_delete= models.CASCADE,
        default= 1
    )
    preço = models.DecimalField(decimal_places=5,max_digits=6)
    status = models.CharField(max_length=150,choices=STATUS_TYPES,default="Aguardando pedido")

    def __str__(self):
        return "%i, %i, %i, %i, %i"%(self.pratos, self.bebidas, self.extras ,self.preco,self.status)


class Delivery(models.Model):
    pratos = models.ManyToManyField(Pratos)
    bebidas= models.ManyToManyField(Bebidas)
    extras = models.ManyToManyField(Extras)
    frete  = models.DecimalField(decimal_places=4,max_digits=6)
    preco  = models.DecimalField(decimal_places=5,max_digits=6)

    def __str__(self):
        return "%i, %i, %i, %i ,%i"%(self.pratos, self.frete, self.bebidas, self.extras, self.preco)
    

class Rodizio(models.Model):
    pratos = models.ManyToManyField(Pratos)
    bebidas= models.ManyToManyField(Bebidas)
    extras = models.ManyToManyField(Extras)
    preco  = models.DecimalField(decimal_places=5,max_digits=6)

    def Preço_Rodizio(self,preco,extras,bebidas):
        self.preco = 50.00
        return "Preço final é %f "%(self.preco + self.extras + self.bebidas)
    
    def __str__(self):
        return "%i, %i, %i, %i"%(self.pratos,self.bebidas,self.extras,self.preco)


class Tipo_de_pedido(TimestampableMixin):
    a_la_carte = models.ManyToManyField(A_la_carte)
    rodizio = models.ManyToManyField(Rodizio)
    delivery = models.ManyToManyField(Delivery)
    status = models.CharField(max_length=150,choices=STATUS_TYPES,default="Aguardando pedido")
'''