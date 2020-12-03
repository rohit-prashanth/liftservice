# Generated by Django 3.1.1 on 2020-12-03 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cust_addres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Phone_no', models.CharField(blank=True, max_length=10)),
                ('house_no', models.CharField(blank=True, max_length=50)),
                ('building_name', models.CharField(blank=True, max_length=50)),
                ('street', models.CharField(blank=True, max_length=60)),
                ('area', models.CharField(blank=True, max_length=30)),
                ('city', models.CharField(blank=True, max_length=30)),
                ('state', models.CharField(blank=True, max_length=30)),
                ('pincode', models.CharField(blank=True, max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Cust_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(blank=True, max_length=30)),
                ('Lastname', models.CharField(blank=True, max_length=30)),
                ('signup_Username', models.EmailField(blank=True, max_length=40)),
                ('signup_Password', models.CharField(blank=True, max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Cust_lift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.CharField(blank=True, max_length=3)),
                ('lift_id', models.CharField(blank=True, max_length=10)),
                ('type', models.CharField(blank=True, max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Cust_login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_Username', models.CharField(blank=True, max_length=30)),
                ('login_Password', models.CharField(blank=True, max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Cust_purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice', models.CharField(blank=True, max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Cust_subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscription_id', models.CharField(blank=True, max_length=15)),
                ('subscription_type', models.CharField(blank=True, max_length=1)),
                ('valid_from', models.DateField(auto_now_add=True)),
                ('valid_to', models.DateField(blank=True)),
                ('invoice_no', models.CharField(blank=True, max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='customer_interface/images')),
            ],
        ),
        migrations.CreateModel(
            name='uthuthiclass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uthuthivar', models.CharField(blank=True, max_length=15)),
            ],
        ),
    ]
