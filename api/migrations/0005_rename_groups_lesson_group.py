# Generated by Django 3.2.9 on 2021-11-27 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20211127_1910'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='groups',
            new_name='group',
        ),
    ]
