# Generated by Django 4.0.7 on 2022-09-14 19:08

# Django
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aa_forum", "0013_personal_messages_migrate_zero_fix"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="discord_dm_on_new_personal_message",
            field=models.BooleanField(default=False),
        ),
    ]
