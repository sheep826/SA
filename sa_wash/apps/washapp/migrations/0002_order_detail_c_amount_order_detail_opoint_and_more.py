# Generated by Django 4.1.4 on 2023-01-03 18:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("washapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order_detail",
            name="C_amount",
            field=models.IntegerField(default=0, verbose_name="花費碳排總量"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="order_detail",
            name="oPoint",
            field=models.IntegerField(default=0, verbose_name="總點數"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="order_detail",
            name="oTotal",
            field=models.IntegerField(default=0, verbose_name="總金額"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="price",
            name="carbon",
            field=models.IntegerField(default=0, verbose_name="碳排量"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="order",
            name="oOrdertime",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="成立時間"
            ),
        ),
        migrations.AlterField(
            model_name="order_detail",
            name="oDelivery",
            field=models.CharField(blank=True, max_length=10, verbose_name="外送員編號"),
        ),
    ]