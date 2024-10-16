# Generated by Django 5.1.2 on 2024-10-15 14:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0014_installmentplan_category_installmentplan_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='installmentplan',
            name='installment_total_number',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='installment_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='installmentplan',
            name='installment_start',
            field=models.PositiveIntegerField(blank=True, default=1, help_text='The installment number to start counting from', validators=[django.core.validators.MinValueValidator(1)], verbose_name='Installment Start'),
        ),
    ]
