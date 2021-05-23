# Generated by Django 3.2.3 on 2021-05-23 22:55

import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

import aa_forum.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="General",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "verbose_name": "AA-Forum",
                "permissions": (
                    ("basic_access", "Can access the AA-SRP module"),
                    (
                        "manage_forum",
                        "Can manage the forum (Categories, topics and messages)",
                    ),
                ),
                "managed": False,
                "default_permissions": (),
            },
        ),
        migrations.CreateModel(
            name="Boards",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="", max_length=254)),
                ("description", models.TextField(blank=True, null=True)),
                ("order", models.IntegerField(default=0)),
            ],
            options={
                "verbose_name": "Board",
                "verbose_name_plural": "Boards",
                "default_permissions": (),
            },
        ),
        migrations.CreateModel(
            name="Categories",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="", max_length=254)),
                ("order", models.IntegerField(default=0)),
                ("collapsible", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "Category",
                "verbose_name_plural": "Categories",
                "default_permissions": (),
            },
        ),
        migrations.CreateModel(
            name="Messages",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "time_posted",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "time_modified",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("subject", models.CharField(default="", max_length=254)),
                ("message", models.TextField(blank=True, null=True)),
                (
                    "board",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="messages",
                        to="aa_forum.boards",
                    ),
                ),
            ],
            options={
                "verbose_name": "Message",
                "verbose_name_plural": "Messages",
                "default_permissions": (),
            },
        ),
        migrations.CreateModel(
            name="Topics",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sticky", models.BooleanField(db_index=True, default=False)),
                ("locked", models.BooleanField(db_index=True, default=False)),
                ("num_views", models.IntegerField(default=0)),
                ("num_replies", models.IntegerField(default=0)),
                (
                    "board",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="topics",
                        to="aa_forum.boards",
                    ),
                ),
                (
                    "first_message",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="aa_forum.messages",
                    ),
                ),
                (
                    "last_message",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="aa_forum.messages",
                    ),
                ),
                (
                    "user_started",
                    models.ForeignKey(
                        on_delete=models.SET(aa_forum.models.get_sentinel_user),
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user_updated",
                    models.ForeignKey(
                        on_delete=models.SET(aa_forum.models.get_sentinel_user),
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Topic",
                "verbose_name_plural": "Topics",
                "default_permissions": (),
            },
        ),
        migrations.AddField(
            model_name="messages",
            name="topic",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="messages",
                to="aa_forum.topics",
            ),
        ),
        migrations.AddField(
            model_name="messages",
            name="user_created",
            field=models.ForeignKey(
                on_delete=models.SET(aa_forum.models.get_sentinel_user),
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="messages",
            name="user_updated",
            field=models.ForeignKey(
                on_delete=models.SET(aa_forum.models.get_sentinel_user),
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="boards",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="boards",
                to="aa_forum.categories",
            ),
        ),
        migrations.AddField(
            model_name="boards",
            name="groups",
            field=models.ManyToManyField(
                blank=True, related_name="aa_forum_boards", to="auth.Group"
            ),
        ),
        migrations.AddField(
            model_name="boards",
            name="parent_board",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="child_boards",
                to="aa_forum.boards",
            ),
        ),
    ]
