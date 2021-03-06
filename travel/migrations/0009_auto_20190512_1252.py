# Generated by Django 2.2.1 on 2019-05-12 12:52

from django.db import migrations, models
import travel.bean.constant


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0008_auto_20190512_0806'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='status',
            field=models.IntegerField(default=travel.bean.constant.ArticleStatus.WAIT),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.IntegerField(default=travel.bean.constant.Role.NORMAL),
        ),
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.CharField(default='667a75f0-3462-4d3e-b12a-97c5aa32b60b', max_length=40),
        ),
    ]
