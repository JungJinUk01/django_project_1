# Generated by Django 5.0.4 on 2024-05-09 00:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("jinuk_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="vehicle",
            name="use",
            field=models.CharField(default="사용", max_length=10),
        ),
    ]