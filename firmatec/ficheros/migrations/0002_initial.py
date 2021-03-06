# Generated by Django 3.2.3 on 2021-08-15 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utils', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ficheros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fichero',
            name='created_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ficheros_fichero_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='fichero',
            name='modified_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ficheros_fichero_modified_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='fichero',
            name='plantas',
            field=models.ManyToManyField(to='utils.Planta'),
        ),
    ]
