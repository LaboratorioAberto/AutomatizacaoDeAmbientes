# Generated by Django 2.1.1 on 2018-10-30 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atuador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('descricao', models.CharField(max_length=100)),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Embarcado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=10)),
                ('localizacao', models.CharField(max_length=20)),
                ('tipo', models.IntegerField()),
                ('firmware', models.CharField(max_length=30)),
                ('atuador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controle.Atuador')),
            ],
        ),
        migrations.CreateModel(
            name='Mqtt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=40)),
                ('porta', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Rede',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=40)),
                ('mascara', models.CharField(max_length=40)),
                ('mac', models.CharField(max_length=40)),
                ('ipGateway', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('descricao', models.CharField(max_length=100)),
                ('data', models.IntegerField()),
                ('sampleRate', models.DecimalField(decimal_places=4, max_digits=4)),
            ],
        ),
        migrations.AddField(
            model_name='embarcado',
            name='mqtt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controle.Mqtt'),
        ),
        migrations.AddField(
            model_name='embarcado',
            name='rede',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controle.Rede'),
        ),
        migrations.AddField(
            model_name='embarcado',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controle.Sensor'),
        ),
    ]
