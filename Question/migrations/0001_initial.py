# Generated by Django 3.2.10 on 2022-01-08 08:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Question",
            fields=[
                ("serial_no", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=100)),
                ("content", models.TextField()),
                ("author", models.CharField(max_length=100)),
                ("slug", models.SlugField(max_length=100)),
                ("subject", models.CharField(max_length=100, null=True)),
                ("timestamp", models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="Answer",
            fields=[
                ("serial_no", models.AutoField(primary_key=True, serialize=False)),
                ("comment", models.TextField()),
                ("timestamp", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "parent",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Question.answer",
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Question.question",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
