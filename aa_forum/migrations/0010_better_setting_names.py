# Generated by Django 4.0.7 on 2022-08-24 18:02

# Django
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("aa_forum", "0009_add_related_names"),
    ]

    operations = [
        migrations.RenameField(
            model_name="setting",
            old_name="default_max_messages",
            new_name="messages_per_page",
        ),
        migrations.RenameField(
            model_name="setting",
            old_name="default_max_topics",
            new_name="topics_per_page",
        ),
    ]
