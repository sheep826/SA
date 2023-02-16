# Generated by Django 4.1.4 on 2023-01-08 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("loginapp", "0002_rename_fkcheck_login_fkcheck"),
    ]

    operations = [
        migrations.CreateModel(
            name="udata",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("UID", models.CharField(max_length=50, verbose_name="使用者編號")),
                ("UAccess", models.CharField(max_length=50, verbose_name="資料請求")),
                ("Upic", models.CharField(max_length=1000, verbose_name="大頭貼")),
            ],
        ),
    ]
