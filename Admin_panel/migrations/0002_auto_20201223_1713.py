# Generated by Django 3.1.3 on 2020-12-23 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_panel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='image',
            field=models.ImageField(upload_to='Admin_panel/images'),
        ),
    ]