# Generated by Django 3.1.7 on 2021-05-01 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
    ]
