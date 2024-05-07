from django.http import HttpResponse
from django.shortcuts import render,HttpResponse,redirect
from service.models import Course,Student
# Create your views here.
def index(request):
    
     return HttpResponse("this is your index")



def course_students(request, course_name):
    
    course = Course.objects.filter(name=course_name)
    data={
        "course":course
    }
    print(data["course"])
    obj2=set()
    for i in course:
        obj=i.instructor
        id=obj.id
        obj2.add(id)
    print(obj2)
    obj2array=[]
    for i in obj2:
        obj2array.append(i)
    
    id=2
    
    students =  Student.objects.filter(id__in=obj2array)
    data={
        "students":students
    }
    
    return render(request, 'course_students.html' ,{'course': course,"students":students})



def addStudent(request):
    if request.method=='POST':
        name1=request.POST.get('name')
        age=request.POST.get('AGE')
        email1=request.POST.get('email')
        date_joined=request.POST.get('DATE_JOINED')
        savesata=Student(name=name1,age=age,email=email1,date_joined=date_joined)
        savesata.save()
        
    return render(request, 'addStudent.html')
def addCourse(request):
    if request.method=='POST':
        name1=request.POST.get('name')
        description=request.POST.get('description')
        instructor=request.POST.get('instructor')
        start_date=request.POST.get('start_date')
        end_date=request.POST.get('end_date')
        print(instructor)
        instructor=Student.objects.get(id=instructor)
        savesata=Course(name=name1,description=description,instructor=instructor,start_date=start_date,end_date=end_date)
        savesata.save()
    data=Student.objects.all()
    ddata={
        "data":data
    }
    print(data)  
    for i in data:
       print(i.name)
    return render(request, 'addCourse.html',{"data":data})

