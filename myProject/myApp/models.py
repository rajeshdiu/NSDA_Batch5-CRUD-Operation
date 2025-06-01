from django.db import models


class StudentModel(models.Model):
    
    Student_Name=models.CharField(max_length=100)
    Department_Name=models.CharField(max_length=100)
    City_Name=models.CharField(max_length=100)
    Student_Age=models.IntegerField()
    
class TeacherModel(models.Model):
    Teacher_Name=models.CharField(max_length=100)
    Address=models.TextField()
    Teacher_age=models.IntegerField()
class CourseMoodel(models.Model):
    Course_Name=models.CharField(max_length=100)
    Course_code=models.CharField(max_length=50)
    
class ProductModel(models.Model):
    Product_Name=models.CharField()
    Product_Code=models.IntegerField()
    Product_Catagori=models.CharField()
       
        

       