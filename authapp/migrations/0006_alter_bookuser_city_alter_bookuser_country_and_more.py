# Generated by Django 4.1.1 on 2022-10-01 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authapp", "0005_bookuser_city_bookuser_country_bookuser_postcode_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookuser",
            name="city",
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name="bookuser",
            name="country",
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name="bookuser",
            name="postcode",
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="bookuser",
            name="street",
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name="bookuser",
            name="street_number",
            field=models.PositiveIntegerField(null=True),
        ),
    ]