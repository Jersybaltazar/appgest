# Generated by Django 4.1.2 on 2023-03-06 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos_close_control', '0004_employee_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='is_used',
            field=models.BooleanField(default=True),
        ),
    ]
