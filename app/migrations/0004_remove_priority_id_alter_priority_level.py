# Generated by Django 5.0.1 on 2024-09-11 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_task_project_alter_priority_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='priority',
            name='id',
        ),
        migrations.AlterField(
            model_name='priority',
            name='level',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]