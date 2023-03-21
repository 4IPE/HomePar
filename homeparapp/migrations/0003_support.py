# Generated by Django 4.1.7 on 2023-03-17 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("homeparapp", "0002_user_alter_info_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="Support",
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
                ("tema", models.CharField(max_length=250, verbose_name="Tema")),
                ("main", models.CharField(max_length=1000, verbose_name="Описание")),
            ],
        ),
    ]