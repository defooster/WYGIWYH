# Generated by Django 5.1.2 on 2024-10-16 18:47

import apps.transactions.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_account_group'),
        ('transactions', '0015_installmentplan_installment_total_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecurringTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('IN', 'Income'), ('EX', 'Expense')], default='EX', max_length=2, verbose_name='Type')),
                ('amount', models.DecimalField(decimal_places=30, max_digits=42, validators=[apps.transactions.validators.validate_non_negative, apps.transactions.validators.validate_decimal_places], verbose_name='Amount')),
                ('description', models.CharField(max_length=500, verbose_name='Description')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End Date')),
                ('recurrence_type', models.CharField(choices=[('day', 'Day(s)'), ('week', 'Week(s)'), ('month', 'Month(s)'), ('year', 'Year(s)')], max_length=7, verbose_name='Recurrence Type')),
                ('recurrence_interval', models.PositiveIntegerField(help_text='Interval of recurrence (e.g., every 2 weeks)', verbose_name='Recurrence Interval')),
                ('last_generated_date', models.DateField(blank=True, null=True, verbose_name='Last Generated Date')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account', verbose_name='Account')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='transactions.transactioncategory', verbose_name='Category')),
                ('tags', models.ManyToManyField(blank=True, to='transactions.transactiontag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Recurring Transaction',
                'verbose_name_plural': 'Recurring Transactions',
                'db_table': 'recurring_transactions',
            },
        ),
        migrations.AddField(
            model_name='transaction',
            name='recurring_transaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='transactions.recurringtransaction', verbose_name='Recurring Transaction'),
        ),
    ]
