# Generated by Django 3.1 on 2022-05-24 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220524_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='fuel',
            field=models.CharField(default='Dīzelis', max_length=30),
        ),
    ]
