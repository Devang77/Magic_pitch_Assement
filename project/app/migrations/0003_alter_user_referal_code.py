# Generated by Django 4.2.3 on 2024-04-07 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_user_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='referal_code',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
