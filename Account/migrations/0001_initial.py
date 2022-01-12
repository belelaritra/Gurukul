# Generated by Django 3.2.10 on 2022-01-12 11:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(default='', max_length=100)),
                ('lname', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(default='', max_length=100)),
                ('roll_number', models.CharField(default='', max_length=12)),
                ('phone_number', models.CharField(default='', max_length=10)),
                ('branch', models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('EE', 'EE'), ('IT', 'IT'), ('AEIE', 'AEIE')], default='CSE', max_length=4)),
                ('year', models.CharField(default='', max_length=4)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
                ('auth_token', models.CharField(max_length=100)),
                ('is_verified', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('safe_mode', models.BooleanField(default=True)),
                ('attempts', models.IntegerField(default=3)),
                ('next_attempt', models.DateTimeField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
