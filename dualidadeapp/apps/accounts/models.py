from django.db import models
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    type = models.CharField('Tipo', max_length=30)
    photo = models.ImageField('Foto', upload_to='foto_perfil')
    cell_phone = models.CharField('Celular', max_length=16)
    area = models.CharField('Area', max_length=30)
    git = models.CharField('Github', max_length=50)
    biography = models.TextField('Biografia', max_length=500)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    class Meta:
        verbose_name = 'Perfil do usuario'
        verbose_name_plural = 'Perfis dos usuarios'

    def __str__(self):
        return self.user.username

