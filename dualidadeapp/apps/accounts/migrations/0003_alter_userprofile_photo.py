# Generated by Django 3.2.5 on 2021-12-01 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_userprofile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(upload_to='foto_perfil', verbose_name='Foto'),
        ),
    ]