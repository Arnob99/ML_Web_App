# Generated by Django 2.2 on 2022-05-18 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment_app', '0006_auto_20220518_2153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='comment',
            new_name='comments',
        ),
    ]