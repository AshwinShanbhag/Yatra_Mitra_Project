# Generated by Django 4.0.5 on 2022-06-29 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_delete_dummylatlng'),
    ]

    operations = [
        migrations.CreateModel(
            name='DummyLatLng',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.DecimalField(decimal_places=15, default=0, max_digits=20)),
                ('lng', models.DecimalField(decimal_places=15, default=0, max_digits=20)),
            ],
        ),
    ]