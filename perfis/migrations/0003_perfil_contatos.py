# Generated by Django 2.0.7 on 2018-08-05 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0002_convite'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='contatos',
            field=models.ManyToManyField(related_name='_perfil_contatos_+', to='perfis.Perfil'),
        ),
    ]
