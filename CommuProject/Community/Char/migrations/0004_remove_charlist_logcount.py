# Generated by Django 2.2.7 on 2019-11-05 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Char', '0003_auto_20191106_0027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='charlist',
            name='logcount',
        ),
    ]
