# Generated by Django 4.0.3 on 2022-04-19 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_grub_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grub',
            name='desc',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='grub',
            name='exp',
            field=models.IntegerField(blank=True, null=True, verbose_name='exp date'),
        ),
        migrations.AlterField(
            model_name='grub',
            name='location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='grub',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]