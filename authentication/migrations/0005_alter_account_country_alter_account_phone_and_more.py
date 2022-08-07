# Generated by Django 4.1 on 2022-08-07 16:15

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("geography", "0002_alter_country_archived"),
        (
            "authentication",
            "0004_alter_account_email_alter_account_email_verified_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="country",
            field=models.ForeignKey(
                help_text="The country of the user",
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                to="geography.country",
            ),
        ),
        migrations.AlterField(
            model_name="account",
            name="phone",
            field=models.BigIntegerField(help_text="The phone of the user", null=True),
        ),
        migrations.AlterField(
            model_name="account",
            name="phone_one_time_code",
            field=models.IntegerField(
                editable=False, help_text="The one time code of the phone", null=True
            ),
        ),
        migrations.AlterField(
            model_name="account",
            name="phone_verified",
            field=models.BooleanField(
                default=False, help_text="Is the phone verified?"
            ),
        ),
        migrations.AlterField(
            model_name="account",
            name="phone_verified_on",
            field=models.DateTimeField(
                editable=False,
                help_text="The date and time when the phone was verified",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="account",
            name="token",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, help_text="The token of the user"
            ),
        ),
    ]