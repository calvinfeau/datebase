# Generated by Django 2.2 on 2019-06-15 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20190615_2007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='attraction',
        ),
    ]
