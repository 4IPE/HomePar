# Generated by Django 4.1.7 on 2023-03-16 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("homeparapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("email", models.CharField(max_length=250, verbose_name="email")),
                ("pasword", models.CharField(max_length=250, verbose_name="pasword")),
            ],
        ),
        migrations.AlterModelOptions(
            name="info",
            options={"verbose_name": "INFO", "verbose_name_plural": "INFO`s"},
        ),
    ]
