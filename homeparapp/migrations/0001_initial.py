# Generated by Django 4.1.7 on 2023-03-15 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Info",
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
                ("city", models.CharField(max_length=250, verbose_name="Адрес")),
                ("price", models.CharField(max_length=15, verbose_name="Цена")),
                ("s", models.CharField(max_length=15, verbose_name="s")),
            ],
        ),
    ]