# Generated by Django 4.1.4 on 2022-12-18 20:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Projects",
            fields=[
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField(blank=True, null=True)),
                ("demo_link", models.CharField(blank=True, max_length=2000, null=True)),
                (
                    "source_link",
                    models.CharField(blank=True, max_length=2000, null=True),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.UUID("6f42451b-151a-4217-b2cb-40a9590f2d8e"),
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
            ],
        ),
    ]