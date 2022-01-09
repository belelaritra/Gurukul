# Generated by Django 3.2.10 on 2022-01-09 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFiles',
            fields=[
                ('serial_no', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('ISBN', models.IntegerField(blank=True, null=True)),
                ('author', models.CharField(max_length=100)),
                ('bookfile', models.FileField(blank=True, upload_to='')),
                ('image_url', models.CharField(blank=True, max_length=100, null=True)),
                ('timestamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]
