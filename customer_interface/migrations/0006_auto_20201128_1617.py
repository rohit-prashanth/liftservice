# Generated by Django 3.1.1 on 2020-11-28 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_interface', '0005_auto_20201128_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cust_detail',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cust_detail',
            name='address_2',
            field=models.CharField(max_length=100),
        ),
    ]
