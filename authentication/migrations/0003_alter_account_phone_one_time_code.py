# Generated by Django 4.1 on 2022-08-07 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0002_account_country_account_phone_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="phone_one_time_code",
            field=models.IntegerField(editable=False, null=True),
        ),
    ]