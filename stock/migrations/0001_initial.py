# Generated by Django 3.1 on 2020-08-26 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0002_auto_20200818_2004'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Quantidade')),
                ('lot', models.CharField(max_length=100, verbose_name='Lote')),
                ('validity', models.DateField(blank=True, null=True, verbose_name='Validade')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Preço')),
                ('coast', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Custo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data de atualização')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Produto')),
            ],
            options={
                'verbose_name': 'Produto em estoque',
                'verbose_name_plural': 'Produtos em estoque',
            },
        ),
    ]