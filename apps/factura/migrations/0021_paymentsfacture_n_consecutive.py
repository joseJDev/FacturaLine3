# Generated by Django 3.2.9 on 2021-12-08 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0020_alter_paymentsfacture_type_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentsfacture',
            name='n_consecutive',
            field=models.IntegerField(null=True),
        ),
    ]
