# Generated by Django 4.0.7 on 2022-08-24 14:43

# Django
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("aa_forum", "0008_populate_default_settings"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lastmessageseen",
            name="topic",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="last_message_seen",
                to="aa_forum.topic",
            ),
        ),
        migrations.AlterField(
            model_name="lastmessageseen",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="aa_forum_last_message_seen",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
