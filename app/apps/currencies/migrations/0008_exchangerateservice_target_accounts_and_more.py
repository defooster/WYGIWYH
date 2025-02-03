# Generated by Django 5.1.5 on 2025-02-03 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_account_name'),
        ('currencies', '0007_exchangerateservice'),
    ]

    operations = [
        migrations.AddField(
            model_name='exchangerateservice',
            name='target_accounts',
            field=models.ManyToManyField(help_text="Select accounts to fetch exchange rates for. Rates will be fetched for each account's currency against their set exchange currency.", related_name='exchange_services', to='accounts.account', verbose_name='Target Accounts'),
        ),
        migrations.AlterField(
            model_name='exchangerateservice',
            name='target_currencies',
            field=models.ManyToManyField(help_text='Select currencies to fetch exchange rates for. Rates will be fetched for each currency against their set exchange currency.', related_name='exchange_services', to='currencies.currency', verbose_name='Target Currencies'),
        ),
    ]
