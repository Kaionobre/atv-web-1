from django.db import models

class Medico(models.Model):
    nome = models.CharField(max_length=50)
    crm = models.CharField(max_length=50)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome
    


# Create your models here.
