# Generated by Django 5.1 on 2024-08-29 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mibits', '0002_alter_nameslist_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='nameslist',
            name='detail',
            field=models.TextField(default=''),
        ),
    ]
