# Generated by Django 4.1 on 2022-08-07 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0005_alter_account_country_alter_account_phone_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="phone",
            field=models.BigIntegerField(
                blank=True, help_text="The phone of the user", null=True
            ),
        ),
    ]
