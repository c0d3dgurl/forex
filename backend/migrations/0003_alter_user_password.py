# Generated by Django 3.2.4 on 2021-09-11 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_user_is_superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=500),
        ),
    ]