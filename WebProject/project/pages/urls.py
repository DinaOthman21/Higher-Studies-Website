from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index,name='index'),
    path('HomePage',views.HomePage,name='HomePage'),
    path('Login',views.Login,name='Login'),
    path('Logout',views.LogoutPage,name='Logout'),
    path('Student',views.StudentPage,name='Student'),
    path('AddStudent',views.AddStudent,name='AddStudent'),
    path('EditStudent/<int:Id>/',views.EditStudent,name='EditStudent'),
    path('updateStudent/<int:Id>/',views.UpdateStudent,name='updateStudent'),
    path('Active',views.ActivePage,name='active'),
    path('Course',views.Course,name='Course'),
    path('AddCourse',views.AddCourse,name='AddCourse'),
    path('EditCourse/<int:Id>/',views.EditCourse,name='EditCourse'),
    path('updateCourse/<int:Id>/',views.UpdateCourse,name='updateCourse'),
    path('RegisterCourse/<int:Id>/',views.RegPage,name='RegisterCourse'),
    path('RegCourse/<int:Id>/',views.RegCourse,name='RegCourse'),
    path('deleteStudent/<int:Id>/',views.deleteStudent,name='deleteStudent'),
    path('deleteCourse/<int:Id>/',views.deleteCourse,name='deleteCourse'),

]
