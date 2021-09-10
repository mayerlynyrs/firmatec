# Generated by Django 3.2.3 on 2021-09-09 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0003_auto_20210909_0937'),
        ('users', '0002_rename_tipo_cta_user_tipo_cuenta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ciudad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='utils.ciudad'),
        ),
        migrations.AlterField(
            model_name='user',
            name='planta',
            field=models.ManyToManyField(help_text='Seleccione solo una planta si el perfil que esta seleccionado es Trabajador.', to='utils.Planta'),
        ),
        migrations.AlterField(
            model_name='user',
            name='provincia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='utils.provincia'),
        ),
        migrations.AlterField(
            model_name='user',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='utils.region'),
        ),
        migrations.AlterField(
            model_name='user',
            name='rut',
            field=models.CharField(error_messages={'unique': 'Ya existe un usuario con este RUT registrado.'}, max_length=12, unique=True),
        ),
    ]
