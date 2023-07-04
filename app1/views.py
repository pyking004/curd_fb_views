from django.shortcuts import render,HttpResponseRedirect
from app1.forms import CourseForm
from app1.models import Course
# Create your views here.

def index(request):
    return render(request,'app1/index.html',{'msg':'This is Index Page'})

def addcourse(request):
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseForm()
        else:
            print("Invalid Form Data")
    context = {'msg':'Add New Course','form':form}
    return render(request,'app1/index.html',context)

def courses(request):
    courses = Course.objects.all()
    return render(request,'app1/courses.html',{'courses':courses})

def updatecourse(request,id):
    if request.method == 'POST':
        course = Course.objects.get(pk=id)
        form = CourseForm(request.POST,instance=course)
        if form.is_valid():
            form.save()
        else:
            print("Invalid form Data")
    else:
        course = Course.objects.get(pk=id)
        form = CourseForm(instance=course)
    return render(request,'app1/update.html',{'form':form})

#delete course
def deletecourse(request,id):
    if request.method == 'POST':
        course = Course.objects.get(pk=id)
        course.delete()
        return HttpResponseRedirect('/app1/courses')
