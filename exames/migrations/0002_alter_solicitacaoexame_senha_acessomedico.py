# Generated by Django 4.2.5 on 2023-10-08 01:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exames', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitacaoexame',
            name='senha',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.CreateModel(
            name='AcessoMedico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificacao', models.CharField(max_length=50)),
                ('tempo_de_acesso', models.IntegerField()),
                ('criado_em', models.DateTimeField()),
                ('data_exames_iniciais', models.DateField()),
                ('data_exames_finais', models.DateField()),
                ('token', models.CharField(blank=True, max_length=20, null=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
