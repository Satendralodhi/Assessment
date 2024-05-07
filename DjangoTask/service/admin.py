from django.contrib import admin

# Register your models here.

from .models import Student, Course
# class student(admin.ModelAdmin):
#     list_display=('id','name','email','age','date_joined' )
# class course(admin.ModelAdmin):
#     list_display=('id','name',  'description','instructor','start_date' ,'end_date' )
admin.site.register(Student)
admin.site.register(Course)