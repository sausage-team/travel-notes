# Generated by Django 2.2.1 on 2019-05-12 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0005_auto_20190512_0330'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articles', to='travel.User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.CharField(default='aa97db42-b25d-47d7-86b6-ea6bfe213ef9', max_length=40),
        ),
    ]
