# Generated by Django 2.2.1 on 2019-05-11 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='uid',
            field=models.CharField(default='<function uuid4 at 0x1037c26a8>', max_length=40),
        ),
    ]
