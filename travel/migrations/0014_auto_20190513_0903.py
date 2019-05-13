# Generated by Django 2.2.1 on 2019-05-13 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0013_auto_20190513_0549'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='icon',
            field=models.TextField(default=b'iVBORw0KGgoAAAANSUhEUgAAAK4AAACVCAYAAADBscGAAAAAAXNSR0IArs4c6QAABBVpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IlhNUCBDb3JlIDUuNC4wIj4KICAgPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4KICAgICAgPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIKICAgICAgICAgICAgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iCiAgICAgICAgICAgIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIgogICAgICAgICAgICB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iCiAgICAgICAgICAgIHhtbG5zOnRpZmY9Imh0dHA6Ly9ucy5hZG9iZS5jb20vdGlmZi8xLjAvIj4KICAgICAgICAgPHhtcE1NOkRlcml2ZWRGcm9tIHJkZjpwYXJzZVR5cGU9IlJlc291cmNlIj4KICAgICAgICAgICAgPHN0UmVmOmluc3RhbmNlSUQ+eG1wLmlpZDo5MEM3NDUzOTJEMEExMUU1QkMxQ0IzRTZCQjY3M0YxNTwvc3RSZWY6aW5zdGFuY2VJRD4KICAgICAgICAgICAgPHN0UmVmOmRvY3VtZW50SUQ+eG1wLmRpZDo5MEM3NDUzQTJEMEExMUU1QkMxQ0IzRTZCQjY3M0YxNTwvc3RSZWY6ZG9jdW1lbnRJRD4KICAgICAgICAgPC94bXBNTTpEZXJpdmVkRnJvbT4KICAgICAgICAgPHhtcE1NOkRvY3VtZW50SUQ+eG1wLmRpZDo5MEM3NDUzQzJEMEExMUU1QkMxQ0IzRTZCQjY3M0YxNTwveG1wTU06RG9jdW1lbnRJRD4KICAgICAgICAgPHhtcE1NOkluc3RhbmNlSUQ+eG1wLmlpZDo5MEM3NDUzQjJEMEExMUU1QkMxQ0IzRTZCQjY3M0Yx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'),
        ),
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.CharField(default='4b596817-b345-4124-a933-84b1f6bbcdd7', max_length=40),
        ),
    ]
