# Generated by Django 3.1.7 on 2021-04-28 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapp', '0006_auto_20210428_1057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='contact',
            new_name='phone',
        ),
    ]
