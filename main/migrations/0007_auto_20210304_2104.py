# Generated by Django 3.1.5 on 2021-03-04 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_entrega_tempo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(default='000', max_length=30)),
                ('nome', models.CharField(default='Arnaldao Sangue Bom', max_length=30)),
                ('funçao', models.CharField(choices=[('CA', 'Carregador'), ('ODMD', 'Operador de Maquina'), ('MC', 'Motorista de Caminhao')], default='nenhuma', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Funcionarios',
            },
        ),
        migrations.CreateModel(
            name='Objeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objetos', models.CharField(choices=[('Pregos', 'pregos'), ('Canos de PVC', 'canos de pvc'), ('Fios de Cobre', 'fios de cobre'), ('Tabuas de Madeira', 'tabuas de madeira'), ('Massa de Revestimento', 'massa'), ('Cimento', 'cimento'), ('Tijolos', 'tijolos')], default='esperando', max_length=25)),
            ],
            options={
                'verbose_name_plural': 'Objetos',
            },
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(default='', max_length=40)),
                ('marca_chassi', models.CharField(default='Iveco', max_length=20)),
                ('motor', models.CharField(default='Honda', max_length=20)),
                ('Tipo_de_Entrega', models.CharField(choices=[('MEP', 'Maquinario Extremamente Pesado'), ('MP', 'Maqunario Pesado'), ('NN', 'Nao Necessita')], default='a definir', max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Veiculos',
            },
        ),
        migrations.RemoveField(
            model_name='entrega',
            name='funçao',
        ),
        migrations.RemoveField(
            model_name='entrega',
            name='matricula',
        ),
        migrations.RemoveField(
            model_name='entrega',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='entrega',
            name='objetos',
        ),
        migrations.RemoveField(
            model_name='entrega',
            name='tempo',
        ),
    ]
