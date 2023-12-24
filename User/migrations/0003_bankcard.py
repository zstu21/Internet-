# Generated by Django 4.2.7 on 2023-12-24 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_remove_users_repassword'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_name', models.CharField(max_length=50)),
                ('balance', models.DecimalField(decimal_places=2, default=10000000.0, max_digits=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.users')),
            ],
        ),
    ]
