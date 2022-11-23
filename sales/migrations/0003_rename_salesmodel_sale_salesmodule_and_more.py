# Generated by Django 4.1.2 on 2022-11-23 08:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sales', '0002_alter_sale_strategy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='salesModel',
            new_name='salesModule',
        ),
        migrations.RenameField(
            model_name='salestask',
            old_name='salesModel',
            new_name='salesModule',
        ),
        migrations.AddField(
            model_name='salesmodule',
            name='head',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='salesmodule',
            name='volts',
            field=models.IntegerField(default=0),
        ),
    ]
