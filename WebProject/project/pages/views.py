from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import  HttpResponseRedirect, JsonResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Student,Courses


# Create your views here.

def Index(request):
    return render(request,'pages/index.html')


def HomePage(request):
    return render(request,'pages/HomePage.html')

# name = admin pass = 123456
def Login(request):
    if request.method == "POST":
        username = request.POST['gabr']
        print(username)
        password = request.POST['psw']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('HomePage')
        else:
            messages.success(request,("Please enter valid credentials"))
            return redirect('Login')
    return render(request,'pages/login.html')

@login_required(login_url='Login')
def LogoutPage(request):
    logout(request)
    return redirect('HomePage')


@login_required(login_url='Login')
def Course(request):
    return render(request,'pages/course.html',{'course':Courses.objects.all()})

 
@login_required(login_url='Login')
def AddCourse(request):
    if request.method == "POST":
        name=request.POST.get('name')
        Id=request.POST.get('id')
        Day=request.POST.get('day')
        dep=request.POST.get('DP')
        hour=request.POST.get('hours')
        hall=request.POST.get('hall')
        data=Courses(CourseID=Id,coursename=name,HallNo=hall,Hourses=hour,Department=dep,CourseDay=Day)
        data.save()
        return HttpResponseRedirect(reverse('Course'),{'course':Courses.objects.all()})
    return render(request,'pages/newcourse.html')

@login_required(login_url='Login')
def ActivePage(request):
    return render(request,'pages/active-inactve.html',{'student':Student.objects.all()})

@login_required(login_url='Login')
def StudentPage(request):
    return render(request,'pages/Student.html',{'student':Student.objects.all()})

@login_required(login_url='Login')
def AddStudent(request):
    if request.method == "POST":
        name=request.POST.get('name')
        print(name)
        Id=request.POST.get('ID')
        Date=request.POST.get('birth')
        Uni=request.POST.get('uni')
        Gen=request.POST.get('gender')
        dep=request.POST.get('DP')
        Stat=request.POST.get('Status')
        Cour1=request.POST.get('course1')
        Cour2=request.POST.get('course2')
        Cour3=request.POST.get('course3')
        data=Student(name=name,ID=Id,date=Date,university=Uni,Gender=Gen,department=dep,statues= Stat,course1=Cour1,course2=Cour2,course3=Cour3)
        data.save()
        return HttpResponseRedirect(reverse('Student'),{'course':Courses.objects.all()})
    return render(request,'pages/New Student.html',{'course':Courses.objects.all()})


@login_required(login_url='Login')
def EditStudent(request,Id):
    display = Student.objects.get(ID=Id)
    return render(request,'pages/Edit Student.html',{'course':Courses.objects.all(),'student':display})

@login_required(login_url='Login')
def UpdateStudent(request,Id):
    if request.method == 'POST':
        UpdateStudent = Student.objects.get(ID=Id)

        UpdateStudent.name=request.POST['m']
        UpdateStudent.ID=request.POST['ID']
        UpdateStudent.date=request.POST['birth']
        UpdateStudent.university=request.POST['uni']
        UpdateStudent.Gender=request.POST['gender']
        UpdateStudent.department=request.POST['DP']
        UpdateStudent.statues= request.POST['Status']
        UpdateStudent.course1=request.POST['course1']
        UpdateStudent.course2=request.POST['course2']
        UpdateStudent.course3=request.POST['course3']

        UpdateStudent.save()

        return HttpResponseRedirect(reverse('Student'))


@login_required(login_url='Login')
def EditCourse(request,Id):
    display = Courses.objects.get(CourseID=Id)
    return render(request,'pages/edit course.html',{'course':Courses.objects.all(),'course':display})


@login_required(login_url='Login')
def UpdateCourse(request,Id):
    if request.method == 'POST':
        UpdateCourse = Courses.objects.get(CourseID=Id)

        UpdateCourse.CourseID=request.POST['ID']
        UpdateCourse.coursename=request.POST['name']
        UpdateCourse.HallNo=request.POST['hall']
        UpdateCourse.Hourses=request.POST['hours']
        UpdateCourse.Department=request.POST['DP']
        UpdateCourse.CourseDay=request.POST['day']
        
        UpdateCourse.save()
        return HttpResponseRedirect(reverse('Course'))



@login_required(login_url='Login')
def RegPage(request,Id):
    display = Student.objects.get(ID=Id)
    return render(request,'pages/Registered Courses.html',{'course':Courses.objects.all(),'student':display})


@login_required(login_url='Login')
def RegCourse(request,Id):
    if request.method == 'POST':
        RegStudent = Student.objects.get(ID=Id)
        
        new = Student(name=RegStudent.name,ID=RegStudent.ID,date=RegStudent.date,university=RegStudent.university,Gender=RegStudent.Gender,department=RegStudent.department,statues=RegStudent.statues,course1=request.POST['course1'],course2=request.POST['course2'],course3=request.POST['course3'])
        new.save()

        return HttpResponseRedirect(reverse('Student'))


def deleteStudent(request,Id):
    stu=Student.objects.get(ID=Id)
    stu.delete()
    return JsonResponse({"messages":"success"})

def deleteCourse(request,Id):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        course=Courses.objects.get(CourseID=Id)
        course.delete()
        return JsonResponse({"messages":"success"})
    return HttpResponseRedirect(reverse('Course'))

