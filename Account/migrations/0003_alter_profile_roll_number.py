# Generated by Django 3.2.8 on 2022-01-04 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_auto_20211220_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='roll_number',
            field=models.CharField(default='', max_length=12),
        ),
    ]
