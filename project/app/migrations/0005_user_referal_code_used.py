# Generated by Django 4.2.3 on 2024-04-07 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_valid_token_remove_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='referal_code_used',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
