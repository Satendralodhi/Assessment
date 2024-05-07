from django.db import models

# Create your models here.

from django.utils import timezone

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    date_joined = models.DateTimeField(default=timezone.now)
    class Meta:
        db_table='student'
    

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # instructor = models.CharField(max_length=100)
    instructor =models.ForeignKey(Student, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    class Meta:
        db_table='course'
    