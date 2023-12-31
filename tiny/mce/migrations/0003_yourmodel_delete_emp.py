# Generated by Django 4.1.5 on 2023-12-28 08:05

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ("mce", "0002_emp_decs"),
    ]

    operations = [
        migrations.CreateModel(
            name="YourModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("content", tinymce.models.HTMLField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(name="Emp",),
    ]
