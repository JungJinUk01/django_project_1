# Generated by Django 5.0.4 on 2024-05-16 05:51

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Vehicle",
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
                ("license_number", models.CharField(max_length=20)),
                ("price", models.BigIntegerField()),
                ("capacity", models.IntegerField()),
                ("license_plate_price", models.BigIntegerField()),
                ("release_date", models.DateField()),
                ("insurance_fee", models.IntegerField()),
                ("vehicle_name", models.CharField(max_length=100)),
                ("monthly_maintenance_cost", models.IntegerField()),
                ("manufacturer", models.CharField(max_length=100)),
                ("daily_tuning_cost", models.IntegerField()),
                ("vehicle_form", models.CharField(max_length=100)),
                ("monthly_depreciation_cost", models.IntegerField()),
                ("model_year", models.IntegerField()),
                ("depreciation_base_year", models.IntegerField()),
                ("vin_number", models.CharField(max_length=17)),
                ("installment", models.CharField(max_length=100)),
                ("engine_type", models.CharField(max_length=20)),
                ("driver_name", models.CharField(max_length=100)),
                ("regular_inspection_date", models.DateField()),
                ("is_active", models.BooleanField(default=True)),
                (
                    "registration_certificate",
                    models.ImageField(upload_to="vehicle_certificates/"),
                ),
                ("has_led_display", models.BooleanField(default=False)),
                ("has_karaoke", models.BooleanField(default=False)),
                ("has_water_heater", models.BooleanField(default=False)),
                ("has_refrigerator", models.BooleanField(default=False)),
                ("has_usb", models.BooleanField(default=False)),
                ("has_tv", models.BooleanField(default=False)),
            ],
        ),
    ]
