# Generated by Django 3.2.7 on 2021-09-12 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20210912_0240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=500),
        ),
    ]
