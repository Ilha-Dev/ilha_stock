# Generated by Django 3.1 on 2020-08-26 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_productstock_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productstock',
            name='quantity',
            field=models.PositiveIntegerField(verbose_name='Quantidade'),
        ),
    ]