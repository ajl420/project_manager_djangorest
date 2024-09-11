# Generated by Django 5.0.1 on 2024-09-11 05:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_priority_project_status_rename_title_task_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.project'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='priority',
            name='level',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]