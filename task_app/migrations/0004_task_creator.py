# Generated by Django 5.0.3 on 2024-04-06 11:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0003_rename_prerety_task_preorety_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='task_app.user'),
        ),
    ]