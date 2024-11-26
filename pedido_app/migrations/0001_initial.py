# Generated by Django 5.1.2 on 2024-11-19 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id_pedido', models.PositiveSmallIntegerField(max_length=6, primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('nombre_cliente', models.CharField(max_length=100)),
                ('producto', models.CharField(max_length=200)),
                ('estado', models.CharField(max_length=100)),
                ('cantidad_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('metodo_entrega', models.CharField(max_length=100)),
            ],
        ),
    ]