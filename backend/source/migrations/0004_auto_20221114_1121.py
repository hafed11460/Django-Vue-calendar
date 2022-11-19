# Generated by Django 3.1 on 2022-11-14 10:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('source', '0003_auto_20220612_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='color',
            field=models.PositiveSmallIntegerField(choices=[(0, 'primary'), (1, 'success'), (2, 'danger'), (3, 'warning'), (4, 'dark')]),
        ),
        migrations.AlterUniqueTogether(
            name='event',
            unique_together={('source', 'date')},
        ),
        migrations.AlterUniqueTogether(
            name='source',
            unique_together={('user', 'name')},
        ),
    ]