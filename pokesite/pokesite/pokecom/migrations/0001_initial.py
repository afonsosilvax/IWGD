# Generated by Django 4.2.6 on 2023-10-25 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carta',
            fields=[
                ('pokemon', models.CharField(max_length=200)),
                ('raridade', models.CharField(max_length=200)),
                ('colecao', models.CharField(max_length=200)),
                ('estado', models.CharField(max_length=200)),
                ('imagem', models.ImageField(default='', upload_to='')),
                ('preco', models.DecimalField(decimal_places=2, default='0.0', max_digits=7)),
                ('vendedor', models.CharField(max_length=200)),
                ('id_api', models.CharField(max_length=200)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Carta_troca',
            fields=[
                ('pokemon', models.CharField(max_length=200)),
                ('raridade', models.CharField(max_length=200)),
                ('colecao', models.CharField(max_length=200)),
                ('estado', models.CharField(max_length=200)),
                ('imagem', models.ImageField(default='', upload_to='')),
                ('preco', models.DecimalField(decimal_places=2, default='0.0', max_digits=7)),
                ('vendedor', models.CharField(max_length=200)),
                ('trade1', models.CharField(max_length=200)),
                ('trade2', models.CharField(max_length=200)),
                ('id_api', models.CharField(max_length=200)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Torneio',
            fields=[
                ('nome_torneio', models.CharField(max_length=200)),
                ('pais', models.CharField(max_length=200)),
                ('loja', models.CharField(max_length=200)),
                ('nome_organizador', models.CharField(max_length=200)),
                ('data', models.DateTimeField()),
                ('premio', models.IntegerField(default='0')),
                ('part', models.CharField(max_length=1000000)),
                ('num_part', models.PositiveIntegerField(default='0')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Organizador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_org', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
