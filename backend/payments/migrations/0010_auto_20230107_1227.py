# Generated by Django 3.1 on 2023-01-07 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0009_auto_20230107_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]