# Generated by Django 5.0.6 on 2024-05-30 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0002_alter_myuser_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='myuser',
            name='code',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='codeProject',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='type',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
