# Generated by Django 4.1 on 2023-01-07 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Broker", "0003_stock_high_price_stock_low_price_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Option",
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
                ("Expiry", models.DateField()),
                ("Strike", models.FloatField()),
                (
                    "Opt_Type",
                    models.CharField(
                        choices=[("CE", "CE"), ("PE", "PE")], max_length=2
                    ),
                ),
                ("EOD_Price", models.FloatField(null=True)),
                ("Expected_Price", models.FloatField(null=True)),
                (
                    "Stock",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Broker.stock"
                    ),
                ),
            ],
        ),
    ]
