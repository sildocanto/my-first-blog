# Generated by Django 2.0.13 on 2019-03-03 21:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('denuncia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidente',
            name='pro_email',
            field=models.EmailField(max_length=35, null=True),
        ),
        migrations.AlterField(
            model_name='incidente',
            name='pro_vto_libreta',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='incidente',
            name='ter_aseguradora',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='incidente',
            name='ter_cedula_conductor',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='incidente',
            name='ter_matricula',
            field=models.CharField(max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='incidente',
            name='ter_nombre_conductor',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='incidente',
            name='ter_telefono_conductor',
            field=models.CharField(max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='incidente',
            name='usuario_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='denuncia.Usuario'),
        ),
    ]