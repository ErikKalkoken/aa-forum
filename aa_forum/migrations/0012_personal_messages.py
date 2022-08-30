# Generated by Django 4.0.7 on 2022-08-30 20:17

# Django
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

# ckEditor
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("aa_forum", "0011_userprofile"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="personalmessage",
            name="slug",
        ),
        migrations.AddField(
            model_name="personalmessage",
            name="deleted_by_recipient",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="personalmessage",
            name="deleted_by_sender",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="personalmessage",
            name="message_head",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="replies",
                to="aa_forum.personalmessage",
            ),
        ),
        migrations.AlterField(
            model_name="personalmessage",
            name="message",
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name="personalmessage",
            name="recipient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="personalmessage",
            name="sender",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
