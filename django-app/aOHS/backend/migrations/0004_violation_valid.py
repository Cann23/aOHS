# Generated by Django 3.2.9 on 2022-01-18 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_worker_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='violation',
            name='valid',
            field=models.BooleanField(default=True),
        ),
    ]