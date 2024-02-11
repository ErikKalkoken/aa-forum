# Generated by Django 4.2.10 on 2024-02-10 23:43

# Django
from django.db import migrations

# CKEditor
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ("aa_forum", "0016_fix_quotation_marks"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="message",
            field=django_ckeditor_5.fields.CKEditor5Field(),
        ),
        migrations.AlterField(
            model_name="personalmessage",
            name="message",
            field=django_ckeditor_5.fields.CKEditor5Field(),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="signature",
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True),
        ),
    ]
