# Generated by Django 3.2.8 on 2022-09-14 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='nombre ')),
                ('apellido', models.CharField(max_length=100, verbose_name='apellido ')),
                ('imagen', models.ImageField(null=True, upload_to='imagenes/', verbose_name='imagen')),
                ('telefono', models.CharField(max_length=100, verbose_name='telefono ')),
                ('direccion', models.CharField(max_length=100, verbose_name='direccion ')),
            ],
        ),
    ]