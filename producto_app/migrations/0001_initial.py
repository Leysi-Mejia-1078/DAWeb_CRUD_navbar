# Generated by Django 5.1.2 on 2024-11-19 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.PositiveSmallIntegerField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=100)),
                ('material', models.CharField(max_length=100)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=6)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tamano', models.CharField(max_length=50)),
            ],
        ),
    ]