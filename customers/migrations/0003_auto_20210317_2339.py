# Generated by Django 3.1.7 on 2021-03-17 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_customer_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='cumulative_payments',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customer',
            name='cumulative_purchases',
            field=models.IntegerField(default=0),
        ),
    ]
