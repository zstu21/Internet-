# Generated by Django 4.2.7 on 2023-12-24 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_users_use_balance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='use_balance',
        ),
    ]
