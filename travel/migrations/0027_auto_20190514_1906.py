# Generated by Django 2.2.1 on 2019-05-14 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0026_auto_20190514_1855'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='id_card',
            new_name='phone',
        ),
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.CharField(default='ada21004-600b-495f-bda7-93e8666abc66', max_length=40),
        ),
    ]
