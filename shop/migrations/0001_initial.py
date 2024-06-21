# Generated by Django 4.2.13 on 2024-06-20 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("title", models.CharField(max_length=500)),
                ("price", models.FloatField()),
                ("discount_price", models.FloatField()),
                ("category", models.CharField(max_length=500)),
                ("description", models.TextField()),
                ("image", models.CharField(max_length=1000)),
            ],
        ),
    ]
