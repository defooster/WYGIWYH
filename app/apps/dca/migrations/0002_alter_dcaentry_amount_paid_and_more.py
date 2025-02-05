# Generated by Django 5.1.2 on 2024-11-13 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dca', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dcaentry',
            name='amount_paid',
            field=models.DecimalField(decimal_places=30, max_digits=42, verbose_name='Amount Paid'),
        ),
        migrations.AlterField(
            model_name='dcaentry',
            name='amount_received',
            field=models.DecimalField(decimal_places=30, max_digits=42, verbose_name='Amount Received'),
        ),
    ]
