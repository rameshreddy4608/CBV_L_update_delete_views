# Generated by Django 4.2 on 2023-05-20 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_name_school_school'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='school',
            new_name='name',
        ),
    ]