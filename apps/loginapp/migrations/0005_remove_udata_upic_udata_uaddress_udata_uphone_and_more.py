# Generated by Django 4.1.4 on 2023-01-12 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("loginapp", "0004_remove_login_raccesscode"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="udata",
            name="Upic",
        ),
        migrations.AddField(
            model_name="udata",
            name="uaddress",
            field=models.CharField(max_length=100, null=True, verbose_name="寄取地址"),
        ),
        migrations.AddField(
            model_name="udata",
            name="uphone",
            field=models.IntegerField(null=True, verbose_name="聯絡電話"),
        ),
        migrations.AddField(
            model_name="udata",
            name="wpoint",
            field=models.IntegerField(null=True, verbose_name="智慧喜點數"),
        ),
    ]
