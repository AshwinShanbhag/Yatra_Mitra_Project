# Generated by Django 4.0.5 on 2022-07-11 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0040_profile_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile',
            new_name='user',
        ),
    ]