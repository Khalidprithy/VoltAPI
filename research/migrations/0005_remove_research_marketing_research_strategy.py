# Generated by Django 4.1.2 on 2022-11-26 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('strategy', '0003_remove_strategy_success_strategy_success_high_and_more'),
        ('research', '0004_research_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='research',
            name='marketing',
        ),
        migrations.AddField(
            model_name='research',
            name='strategy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='strategy.strategy'),
        ),
    ]
