# Generated by Django 3.2.7 on 2021-09-12 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_alter_user_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signal',
            name='action',
        ),
        migrations.RemoveField(
            model_name='signal',
            name='currency',
        ),
    ]
