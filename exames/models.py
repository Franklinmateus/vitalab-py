from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

class TiposExames(models.Model):
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
    
class SolicitacaoExame(models.Model):
    choice_status = (
        ('E', 'Em análise'),
        ('F', 'Finalizado')
    )
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    exame = models.ForeignKey(TiposExames, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=2, choices=choice_status)
    resultado = models.FileField(upload_to="resultados", null=True, blank=True)
    requer_senha = models.BooleanField(default=True)
    senha = models.CharField(max_length=8, null=True, blank=True)

    def __str__(self):
        return f'{self.usuario} | {self.exame.nome}'
    
    def badge_template(self):
        if self.status == 'E':
            classes = 'bg-warning text-dark'
            texto = 'Em análise.'
        elif self.status == 'F':
            classes = 'bg-success'
            texto = 'Finalizado'
            
        return mark_safe(f'<span class="badge {classes}">{texto}</span>')
    
class PedidosExame(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    exames = models.ManyToManyField(SolicitacaoExame)
    agendado = models.BooleanField(default=True)
    data = models.DateField()

    def __str__(self):
        return f'{self.usuario} | {self.data}'