# Generated by Django 4.1.4 on 2022-12-21 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0005_alter_project_id_alter_review_id_alter_tag_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="featured_image",
            field=models.ImageField(
                blank=True, default="default.jpg", null=True, upload_to=""
            ),
        ),
    ]