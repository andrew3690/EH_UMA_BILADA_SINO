# Generated by Django 3.1.7 on 2021-03-07 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20210307_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrega',
            name='veiculo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.veiculo'),
        ),
    ]