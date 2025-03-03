import datetime
from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.utils.timezone import make_aware
from datetime import datetime


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=50)
    data_cadastro = models.DateTimeField(default=lambda: make_aware(datetime.now()))

    def __str__(self):
        return self.nome

class Obra(models.Model):
    STATUS_PARCELADO_CHOICES = [
        (True, 'Sim'),(False, 'Não'),
    ]
    
    id_obra = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    endereco_obra = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)
    tempo_obra = models.CharField(max_length=20)
    data_inicio = models.DateField()
    data_conclusao = models.DateField(null=True, blank=True)
    valor_obra = models.DecimalField(max_digits=12, decimal_places=2)
    status_parcelado = models.BooleanField(choices=STATUS_PARCELADO_CHOICES, default=False)
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id_obra} - {self.endereco_obra}"
