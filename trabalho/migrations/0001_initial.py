# Generated by Django 4.2.1 on 2023-06-27 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('Semestreingresso', models.IntegerField(verbose_name='Semestre de ingresso')),
                ('Anoingresso', models.IntegerField(verbose_name='Ano de ingresso')),
                ('nota', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Nota')),
                ('situacao', models.CharField(max_length=9, verbose_name='Nome')),
            ],
        ),
    ]
