from django.db import models

class Medico(models.Model):
    nome = models.CharField(max_length=50)
    crm = models.CharField(max_length=50)
    idade = models.IntegerField()
    imagem = models.ImageField(upload_to='medico/', null=True, blank=True)

    def __str__(self):
        return self.nome
    


# Create your models here.
