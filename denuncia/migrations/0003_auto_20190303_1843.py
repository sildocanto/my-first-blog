# Generated by Django 2.0.13 on 2019-03-03 21:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('denuncia', '0002_auto_20190303_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidente',
            name='pro_email',
            field=models.EmailField(blank=True, max_length=35, null=True),
        ),
        migrations.AlterField(
            model_name='incidente',
            name='pro_vto_libreta',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='incidente',
            name='ter_aseguradora',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='incidente',
            name='ter_cedula_conductor',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='incidente',
            name='ter_matricula',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='incidente',
            name='ter_nombre_conductor',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='incidente',
            name='ter_telefono_conductor',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
    ]
