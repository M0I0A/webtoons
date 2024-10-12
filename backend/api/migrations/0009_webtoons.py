# Generated by Django 5.1.1 on 2024-10-11 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0008_auto_20230301_0444"),
    ]

    operations = [
        migrations.CreateModel(
            name="webtoons",
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
                ("title", models.CharField(max_length=50)),
                ("thumbnile", models.ImageField(upload_to="thumbline")),
                ("description", models.TextField()),
            ],
        ),
    ]
