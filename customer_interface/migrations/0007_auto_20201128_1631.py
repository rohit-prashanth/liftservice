# Generated by Django 3.1.1 on 2020-11-28 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_interface', '0006_auto_20201128_1617'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cust_detail',
            old_name='address',
            new_name='Address',
        ),
        migrations.RenameField(
            model_name='cust_detail',
            old_name='address_2',
            new_name='Address_2',
        ),
        migrations.RenameField(
            model_name='cust_detail',
            old_name='city',
            new_name='City',
        ),
        migrations.RenameField(
            model_name='cust_detail',
            old_name='fname',
            new_name='Firstname',
        ),
        migrations.RenameField(
            model_name='cust_detail',
            old_name='lname',
            new_name='Lastname',
        ),
        migrations.RenameField(
            model_name='cust_detail',
            old_name='password',
            new_name='Password',
        ),
        migrations.RenameField(
            model_name='cust_detail',
            old_name='state',
            new_name='Password_Again',
        ),
        migrations.RenameField(
            model_name='cust_detail',
            old_name='phone_no',
            new_name='Phone_no',
        ),
        migrations.RenameField(
            model_name='cust_detail',
            old_name='zip',
            new_name='State',
        ),
        migrations.RenameField(
            model_name='cust_detail',
            old_name='username',
            new_name='Username',
        ),
        migrations.AddField(
            model_name='cust_detail',
            name='Zip',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]