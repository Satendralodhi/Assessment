# Generated by Django 5.0.4 on 2024-05-06 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_alter_course_instructor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='instructor',
        ),
    ]
