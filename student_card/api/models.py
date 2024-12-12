from django.db import models

class StudentCard(models.Model):
    nome = models.CharField(max_length=255)
    ra = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=14)
    curso = models.CharField(max_length=100)
    ano_fabricacao = models.IntegerField()
    endereco = models.TextField()
    imagem = models.ImageField(upload_to='images/')
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)

    def __str__(self):
        return self.nome

# define o modelo que representa um cartão de estudante com todas essas variaveis