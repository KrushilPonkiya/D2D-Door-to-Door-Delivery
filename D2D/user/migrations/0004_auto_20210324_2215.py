# Generated by Django 3.1.4 on 2021-03-24 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210324_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='Phone_Number',
            field=models.IntegerField(blank=True, max_length=10),
        ),
    ]
