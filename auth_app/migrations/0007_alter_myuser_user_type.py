# Generated by Django 5.0.6 on 2024-05-30 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0006_myuser_codesklad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='user_type',
            field=models.IntegerField(default=2),
        ),
    ]
