# Generated by Django 4.0.4 on 2022-05-26 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_todo_priority'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='iaCompleted',
            new_name='isCompleted',
        ),
    ]
