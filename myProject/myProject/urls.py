from django.contrib import admin
from django.urls import path

from myProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage,name="homePage"),
    path('student/', addStudent,name="addStudent"),
    path('student/student_list/', studentList,name="studentList"),
    path('teacherlist/',teacherList,name='teacherList'),
    path('addteacher/',addTeacher,name='addTeacher'),
    path('courselist/',courseList,name='courselist'),
    path('addcourse/',addcourse,name='addcourse'),
    path('Product/',Productpage,name='Product'),
    path('deleteStudent/<str:myid>',deleteStudent,name='deleteStudent'),
    path('editStudent/<str:myid>',editStudent,name='editStudent'),
]
