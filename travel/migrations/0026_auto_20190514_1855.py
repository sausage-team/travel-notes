# Generated by Django 2.2.1 on 2019-05-14 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0025_auto_20190514_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='cover',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='article',
            name='preview',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.CharField(default='72ce94c9-ad2c-4a02-be5d-118acca0cf31', max_length=40),
        ),
    ]
