# Generated by Django 3.0.2 on 2020-11-08 07:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SystemNotification', '0005_auto_20201108_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationhistory',
            name='notification',
            field=models.ForeignKey(blank=True, db_column='notification', null=True, on_delete=django.db.models.deletion.CASCADE, to='SystemNotification.Notification'),
        ),
        migrations.AlterField(
            model_name='notificationhistory',
            name='period',
            field=models.DateTimeField(db_column='period', db_index=True, default=datetime.datetime(2020, 11, 8, 10, 37, 27, 563925)),
        ),
    ]