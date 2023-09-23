from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    Name = models.CharField(max_length=25,null=True)
    Email_id = models.EmailField(null=True)
    Contact_Number = models.CharField(max_length=10,null=True)
    address = models.TextField(null=True)
    Roll_no = models.IntegerField(null=True)
    # Course = models.ForeignKey(Course, on_delete=models.CASCADE,null=True)
    Age = models.IntegerField(null=True)
    photo=models.ImageField(upload_to='profile',null=True)


class Course(models.Model):
    Name=models.CharField(max_length=100)
    Description=models.TextField()
    Duration=models.CharField(max_length=100, null=True)
    Fee=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.Name
#
# class Student(models.Model):
#     student = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
#     Name=models.CharField(max_length=25)
#     Roll_no=models.IntegerField()
#     Course=models.ForeignKey(Course,on_delete=models.CASCADE)
#     Age=models.IntegerField()
#     Contact_Number=models.CharField(max_length=10)
    # Email_id =models.EmailField()

    def __str__(self):
        return self.Name

class Attendance(models.Model):
    student=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    date=models.DateField()
    attendance=models.CharField(max_length=25)
    time=models.TimeField()

class Notification(models.Model):
    subject=models.CharField(max_length=100)
    content=models.TextField()
    updated=models.DateTimeField(auto_now_add=True)
    created=models.TimeField()

    class Meta:
        ordering=['-updated','-created']




