# Generated by Django 4.1.2 on 2022-11-26 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0003_platform_social_remove_marketing_success_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='social',
            name='completed',
        ),
        migrations.AddField(
            model_name='social',
            name='completed_posts',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='social',
            name='expected_posts',
            field=models.IntegerField(default=1),
        ),
    ]
