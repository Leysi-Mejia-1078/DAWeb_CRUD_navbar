# Generated by Django 5.1.2 on 2024-11-16 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.PositiveSmallIntegerField(max_length=100, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.PositiveBigIntegerField(max_length=10)),
                ('correo', models.CharField(max_length=100)),
                ('membresia', models.CharField(max_length=100)),
            ],
        ),
    ]
