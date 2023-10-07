from django.db import models

class TiposExames (models.Model):
    tipo_choices = (
        ('I', 'Exame de imagem'),
        ('S', 'Exame de sangue')
    )
    nome = models.CharField(max_length=150)
    tipo = models.CharField(max_length=1, choices=tipo_choices)
    preco = models.FloatField()
    disponivel = models.BooleanField(default=True)
    horario_inicial = models.IntegerField()
    horario_final = models.IntegerField()
    
    def __str__(self):
        return self.nome
    