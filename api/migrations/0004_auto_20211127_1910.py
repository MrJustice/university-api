# Generated by Django 3.2.9 on 2021-11-27 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20211126_1314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='groups',
        ),
        migrations.AddField(
            model_name='lesson',
            name='groups',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='api.group'),
        ),
    ]
