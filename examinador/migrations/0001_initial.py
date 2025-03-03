# Generated by Django 5.1.5 on 2025-01-29 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Pregunta",
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
                ("pregunta", models.CharField(max_length=255)),
                ("respuesta1", models.CharField(max_length=255)),
                ("respuesta2", models.CharField(max_length=255)),
                ("respuesta3", models.CharField(max_length=255)),
                ("respuesta4", models.CharField(max_length=255)),
                ("correcta", models.IntegerField()),
                ("justificacion", models.CharField(max_length=255)),
                ("normativa", models.CharField(max_length=255)),
            ],
        ),
    ]
