# Generated by Django 4.1.1 on 2022-09-24 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="OrderStats",
            fields=[
                ("odoo_id", models.AutoField(primary_key=True, serialize=False)),
                ("user_id", models.IntegerField()),
                ("created", models.DateTimeField()),
            ],
            options={
                "db_table": "rpc_order_stats",
            },
        ),
        migrations.CreateModel(
            name="PosCategory",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("parent_id", models.IntegerField()),
                ("name", models.CharField(max_length=200)),
                ("display_name", models.CharField(max_length=200)),
            ],
            options={
                "db_table": "rpc_pos_category",
            },
        ),
        migrations.CreateModel(
            name="ProductAttribute",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=200)),
            ],
            options={
                "db_table": "rpc_product_attribute",
            },
        ),
        migrations.CreateModel(
            name="ProductAttributeValue",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("attribute_id", models.IntegerField()),
                ("name", models.CharField(max_length=200)),
                ("attribute_name", models.CharField(max_length=200)),
            ],
            options={
                "db_table": "rpc_product_attribute_value",
            },
        ),
        migrations.CreateModel(
            name="ProductAttributeValueOrder",
            fields=[
                ("attr_val_id", models.AutoField(primary_key=True, serialize=False)),
                ("sort", models.IntegerField()),
            ],
            options={
                "db_table": "rpc_product_attribute_value_order",
            },
        ),
        migrations.CreateModel(
            name="ProductCategory",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("parent_id", models.IntegerField()),
                ("name", models.CharField(max_length=200)),
                ("display_name", models.CharField(max_length=200)),
                ("weight",models.DecimalField(max_digits=5, decimal_places=2, default=0.0))
            ],
            options={
                "db_table": "rpc_product_category",
            },
        ),
        migrations.CreateModel(
            name="ProductStats",
            fields=[
                ("odoo_id", models.AutoField(primary_key=True, serialize=False)),
                ("client_id", models.IntegerField()),
                ("user_id", models.IntegerField()),
                ("created", models.DateTimeField()),
            ],
            options={
                "db_table": "rpc_product_stats",
            },
        ),
        migrations.CreateModel(
            name="ResPartner",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=200)),
                ("vat", models.CharField(max_length=200)),
            ],
            options={
                "db_table": "rpc_res_partner",
            },
        ),
    ]
