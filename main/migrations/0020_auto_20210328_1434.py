# Generated by Django 3.1.7 on 2021-03-28 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20210316_0933'),
    ]

    operations = [
        migrations.RenameField(
            model_name='objeto',
            old_name='objetos',
            new_name='objeto',
        ),
        migrations.RemoveField(
            model_name='entrega',
            name='status',
        ),
        migrations.AddField(
            model_name='funcionario',
            name='em_uso',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='objeto',
            name='espaco',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='objeto',
            name='quantidade',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='veiculo',
            name='capacidade',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='veiculo',
            name='em_uso',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='veiculo',
            name='espaco_usado',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Loja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificacao', models.CharField(default='loja', max_length=200)),
                ('city', models.CharField(default='city', max_length=200)),
                ('states', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], default='states', max_length=200)),
                ('entregas', models.ManyToManyField(to='main.Entrega')),
                ('veiculos', models.ManyToManyField(to='main.Objeto')),
            ],
        ),
    ]