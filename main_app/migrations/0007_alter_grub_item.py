# Generated by Django 4.0.3 on 2022-04-19 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_grub_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grub',
            name='item',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
