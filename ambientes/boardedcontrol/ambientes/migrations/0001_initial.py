# Generated by Django 2.1.1 on 2018-11-01 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ambiente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=5)),
                ('bloco', models.CharField(max_length=15)),
                ('sala', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('modelo', models.CharField(max_length=30)),
                ('serial', models.CharField(max_length=30, unique=True)),
                ('ambiente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ambientes.Ambiente')),
            ],
        ),
    ]
