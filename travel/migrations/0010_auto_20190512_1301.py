# Generated by Django 2.2.1 on 2019-05-12 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0009_auto_20190512_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.CharField(default='606ee390-42ed-4270-b2e4-e4aa733d1a3d', max_length=40),
        ),
    ]