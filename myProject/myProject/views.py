from django.shortcuts import render,redirect
from myApp.models import *

def homePage(req):
    
    return render(req,"homePage.html")

def addStudent(req):
    
    if req.method=='POST':
        
        student=StudentModel(
            Student_Name=req.POST.get("Student_Name"),
            Department_Name=req.POST.get("Department_Name"),
            City_Name=req.POST.get("City_Name"),
            Student_Age=req.POST.get("Student_Age"),
        )
        
        student.save()
        return redirect("studentList")

    return render(req,"addStudent.html")

def studentList(req):
    
    context={
        'data':StudentModel.objects.all()
    }
    
    return render(req,"studentList.html",context)
def teacherList(req):
    context ={
        'Teachers' : TeacherModel.objects.all()
    }
    return render (req, 'TeacherList.html', context)
def addTeacher(req):
    if req.method=='POST':
        teacher= TeacherModel(
         Teacher_Name = req.POST.get('Teacher_Name'),
         Address=req.POST.get('Address'),
         Teacher_age=req.POST.get('Teacher_age'), 
        )
        teacher.save()
        return redirect ('teacherList')
    return render (req,"addTeacher.html")
def courseList(req):
    context ={
        'courses' : CourseMoodel.objects.all()
    }
    return render (req,"CourseList.html",context)
def addcourse(req):
     if req.method=='POST':
        course= CourseMoodel(
         Course_Name = req.POST.get('Course_Name'),
         Course_code=req.POST.get('Course_code'),
         
        )
        course.save()
        return redirect ('courselist')
     return render (req,"addCourse.html")
 
 
def Productpage (req):
    
    context={
        'data':ProductModel.objects.all()
    }
    
    return render(req,"Product.html",context)
 
 
def Productpage(req):
    if req.method=='POST':
        course= ProductModel(
        Product_Name= req.POST.get('Product_Name'),
        Product_Code=req.POST.get('Product_Code'),
        Product_Catagori=req.POST.get('Product_Catagori'),
         
        )
        course.save()
        return redirect ('Product')
    return render (req,"Product.html")


def deleteStudent(req,myid):
    
    student=StudentModel.objects.get(id=myid)
    
    student.delete()
    
    return redirect("studentList")

def editStudent(req,myid):
    
    student=StudentModel.objects.get(id=myid)
    context={
        'data':student
    }
    if req.method=='POST':
        student=StudentModel(
            id=myid,
            Student_Name=req.POST.get("Student_Name"),
            Department_Name=req.POST.get("Department_Name"),
            City_Name=req.POST.get("City_Name"),
            Student_Age=req.POST.get("Student_Age"),
        )
        
        student.save()
        return redirect("studentList")
    
    return render(req,"editStudent.html",context)