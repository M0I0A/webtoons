# Generated by Django 5.1.1 on 2024-10-11 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0011_webtoons_creator_webtoons_genre_alter_webtoons_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="webtoons",
            name="creator",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="webtoons",
            name="genre",
            field=models.CharField(max_length=50, null=True),
        ),
    ]
