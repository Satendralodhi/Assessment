# Generated by Django 5.0.4 on 2024-05-06 13:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_alter_course_instructor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instructorname', to='service.student'),
        ),
    ]
