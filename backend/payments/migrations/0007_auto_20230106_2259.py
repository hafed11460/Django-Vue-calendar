# Generated by Django 3.1 on 2023-01-06 21:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0006_auto_20230106_2241'),
    ]

    operations = [
        migrations.RenameField(
            model_name='package',
            old_name='pakage_type',
            new_name='package_type',
        ),
        migrations.RenameField(
            model_name='package',
            old_name='two_year_price',
            new_name='two_years_price',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='order_date',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='order_len',
        ),
        migrations.AddField(
            model_name='subscription',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subscription',
            name='subscribe_duration',
            field=models.CharField(choices=[('SIX_MONTHS', '6 Months'), ('ONE_YEAR', '1 year'), ('TWO_YEARS', '2 Years')], default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]
