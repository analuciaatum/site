from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver



class Usuario(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]
    
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)  
    celular = models.CharField(max_length=15) 
    date = models.DateField()
    email = models.EmailField(unique=True)
    sexo = models.IntegerField(choices=SEXO_CHOICES)
    
    
    
    def __str__(self):
        return self.nome

class Login(models.Model):
    email = models.EmailField(max_length=254)
    cpf = models.CharField(max_length=11)

@receiver(post_save, sender=Usuario)
def create_login(sender, instance, created, **kwargs):
    if created:
        Login.objects.create(email=instance.email, cpf=instance.cpf)




class Agendamento(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    data_consulta = models.DateField()
    tratamento = models.CharField(max_length=255)
    medico = models.CharField(max_length=255)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)  # Definindo como CharField com escolhas
    def __str__(self):
        return f'{self.nome} - {self.data_consulta}'













