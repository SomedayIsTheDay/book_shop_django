# Generated by Django 4.1.1 on 2022-10-01 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0003_alter_book_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="book",
            options={"ordering": ["-name"]},
        ),
    ]
