# Generated by Django 5.0.4 on 2024-05-06 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_alter_course_instructor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='instructor',
            field=models.CharField(max_length=100),
        ),
    ]
