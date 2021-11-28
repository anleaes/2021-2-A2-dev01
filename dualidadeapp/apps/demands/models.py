from django.db import models

# Create your models here.

class Demand(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    title = models.CharField('Titulo', max_length=100, null=False, blank=False) 
    description = models.CharField('Descricao', max_length=200)   
    deadline = models.DateField('Prazo Final', auto_now=False, auto_now_add=False)
    type = models.CharField('Tipo', max_length=30, null=False, blank=False)
    STATUS_CHOICES = (
        ('Em andamento', 'Em andamento'),
        ('Finalizado', 'Finalizado'),
        ('Cancelado', 'Cancelado'),
    )
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, null=True, blank=True, default='Em andamento')
    repository = models.CharField('Repositorio', max_length=100)
    
    class Meta:
        verbose_name = 'Demanda'
        verbose_name_plural = 'Demandas'
        ordering =['id']

    def __str__(self):
        return self.title