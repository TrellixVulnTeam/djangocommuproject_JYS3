# Generated by Django 2.2.7 on 2019-11-05 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Log', '0002_auto_20191105_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loglist',
            name='charname',
            field=models.CharField(max_length=64, verbose_name='캐릭터 이름'),
        ),
    ]