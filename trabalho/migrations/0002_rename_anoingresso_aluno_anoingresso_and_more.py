# Generated by Django 4.2.1 on 2023-06-27 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trabalho', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aluno',
            old_name='Anoingresso',
            new_name='anoIngresso',
        ),
        migrations.RenameField(
            model_name='aluno',
            old_name='Semestreingresso',
            new_name='semestreIngresso',
        ),
        migrations.AlterField(
            model_name='aluno',
            name='situacao',
            field=models.CharField(max_length=9, verbose_name='Situação'),
        ),
    ]
