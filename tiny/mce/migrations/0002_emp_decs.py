# Generated by Django 4.1.5 on 2023-12-28 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mce", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="emp",
            name="decs",
            field=models.TextField(default="hello"),
            preserve_default=False,
        ),
    ]
