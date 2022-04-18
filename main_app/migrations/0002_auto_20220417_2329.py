# Generated by Django 2.2.12 on 2022-04-17 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grub',
            name='location',
            field=models.CharField(default='Enter an Address', max_length=200),
        ),
        migrations.AddField(
            model_name='grub',
            name='option',
            field=models.CharField(choices=[('P', 'Pick-Up'), ('D', 'Delivery')], default='P', max_length=1),
        ),
    ]