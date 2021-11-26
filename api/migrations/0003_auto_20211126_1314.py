# Generated by Django 3.2.9 on 2021-11-26 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20211126_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='number',
            field=models.CharField(max_length=15, verbose_name='classroom number'),
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=15, unique=True, verbose_name='group name'),
        ),
    ]