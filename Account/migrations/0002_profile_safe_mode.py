# Generated by Django 3.2.10 on 2022-01-08 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Account", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="safe_mode",
            field=models.BooleanField(default=True),
        ),
    ]
