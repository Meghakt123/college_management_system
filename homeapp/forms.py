from django import forms
from django.contrib.auth.forms import UserCreationForm

from homeapp.models import Course, CustomUser, Notification
from django.forms import ModelForm
from.models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model= Course
        fields= '__all__'


# class TeacherForm(forms.ModelForm):
#     class Meta:
#         model= Teacher
#         fields= ('Name','Contact_Number','address')

class UserForm(UserCreationForm):
    class Meta:
        model= CustomUser
        fields= ('Name','Contact_Number','address','email','username','password1','password2')

class StudentForm(UserCreationForm):
    class Meta:
        model= CustomUser
        fields= ('Name','username','Roll_no','Age','address','Contact_Number','email','password1','password2','photo')

class NotificationForm(forms.ModelForm):
    class Meta:
        model=Notification
        fields=('subject','content')





