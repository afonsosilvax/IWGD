# Generated by Django 4.2.6 on 2023-10-17 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carta',
            fields=[
                ('pokemon', models.CharField(max_length=200)),
                ('raridade', models.CharField(max_length=200)),
                ('colecao', models.CharField(max_length=200)),
                ('imagem', models.ImageField(default='', upload_to='')),
                ('preco', models.DecimalField(decimal_places=2, default='0.0', max_digits=7)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
