import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


from homeapp.forms import CourseForm, UserForm, StudentForm,NotificationForm
from homeapp.models import Course, CustomUser, Attendance, Notification


# Create your views here.
def admin_home(request):
    return render(request,'admin_template/skydash.html')

def course(request):
    data = Course.objects.all()
    return render(request,'student_template/Course.html',{'data':data})


def Teachers(request):
    data =CustomUser.objects.filter(is_teacher=True)
    print(data)
    return render(request,'admin_template/Teacher.html',{'data':data})

def add_course(request):
    form = CourseForm
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_view_course')
    return render(request,'admin_template/add_course.html',{'form':form})

def course_update(request,id):
    data =Course.objects.get(id=id)
    form = CourseForm(instance=data)
    if request.method == 'POST':
        form= CourseForm(request.POST or None,instance=data or None)
        if form.is_valid():
            form.save()
            return redirect('Course')
    return render(request,'admin_template/add_course.html',{'form':form})

def course_delete(request,id):
    data =Course.objects.get(id=id)
    data.delete()
    return redirect('Course')

def teacher_registration(request):
    login_form=UserForm()
    if request.method == 'POST':
        login_form =UserForm(request.POST)
        if login_form.is_valid():
            user=login_form.save(commit=False)
            user.is_teacher=True
            user.save()
            messages.info(request,'Teacher Registered Successful')
            return redirect('teacher')
    return render(request,'admin_template/teacher_registration.html', {'login_form':login_form})




def teacher_update(request,id):
    data =CustomUser.objects.get(id=id)
    form = UserForm(instance=data)
    if request.method == 'POST':
        form= UserForm(request.POST or None,instance=data or None)
        if form.is_valid():
            form.save()
            return redirect('teacher')
    return render(request,'admin_template/teacher_registration.html',{'form':form})

def teacher_delete(request,id):
    data =CustomUser.objects.get(id=id)
    data.delete()
    return redirect('teacher')

def Login_view(request):
    if request.method=='POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_superuser:
                return redirect('admin_home')
            elif user.is_student:
                return redirect('student_dashboard')
            elif user.is_teacher:
                return redirect('teacher_dashboard')
        else:
            messages.error(request,'error while login,please try again')
    return render(request,'login_view.html')


def register_page(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_student = True
            user.save()
            messages.info(request,'Student Registered Successful')
            return redirect('student')
    return render(request, 'admin_template/register_page.html', {'form': form})


def Student(request):
    data1 = CustomUser.objects.filter(is_student=True)
    return render(request, 'admin_template/students.html', {'student': data1})


def student_delete(request,id):
    data =CustomUser.objects.get(id=id)
    data.delete()
    return redirect('student')

def profile_page(request):
    data = CustomUser.objects.filter(username=request.user)
    return render(request,'student_template/profile_view.html',{'data':data})


def Student_dashboard(request):
    return render(request,'student_template/student_dashboard.html')


def Teacher_dashboard(request):
    return render(request,'teacher_template/teacher_dashboard.html')


def Attendance_page(request):
    data=CustomUser.objects.filter(is_student=True)
    return render(request,'teacher_template/attendance_page.html',{'data':data})


now=datetime.datetime.now()
def Add_attendance(request,id):
    user =CustomUser.objects.get(id=id)
    att= Attendance.objects.filter(student=user,date=datetime.date.today())
    if att.exists():
        messages.info(request,"today's attendance already marked for the student")
        return redirect('attendance_page')
    else:
        if request.method=='POST':
            attendc=request.POST.get('attendance')
            Attendance(student=user,date=datetime.date.today(),attendance=attendc,time=now.time()).save()
            messages.info(request,"Attendance added successfully")
            return redirect('staff_view_attendance')
    return render(request,'teacher_template/add_attendance.html')

def View_attendance(request):
    value_list=Attendance.objects.values_list('date', flat=True).distinct()
    print(value_list)
    attendance = {}
    print(attendance)
    for value in value_list:
        attendance[value]=Attendance.objects.filter(date=value)
        print(attendance[value])
    return render(request,'admin_template/view_attendance.html',{'attendances': attendance})

def Day_attendance(request,date):
    attendance = Attendance.objects.filter(date=date)
    context = {
        'attendances':attendance,
        'date':date
    }
    return render(request,'teacher_template/day_attendance.html',context)

def add_notification(request):
    # data = Notification.objects.all()
    form = NotificationForm()
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            return redirect('admin_view_notification')
    return render(request,'admin_template/add_notification.html',{'form':form})

def view_notification(request):
    notifications=Notification.objects.all()
    return render(request,'student_template/view_notification.html',{'notifications':notifications})

def index(request):
    return render(request,'index.html')

def admin_home(request):
    return render(request,'admin_template/skydash.html')

def admin_view_notification(request):
    data = Notification.objects.all()
    return render(request,'admin_template/admin_view_notification.html',{'data':data})


def admin_view_course(request):
    data = Course.objects.all()
    return render(request,'admin_template/admin_view_course.html',{'data':data})

def admin_course_update(request,id):
    data =Course.objects.get(id=id)
    form = CourseForm(instance=data)
    if request.method == 'POST':
        form= CourseForm(request.POST or None,instance=data or None)
        if form.is_valid():
            form.save()
            return redirect('admin_view_course')
    return render(request,'admin_template/add_course.html',{'form':form})


def admin_course_delete(request,id):
    data =Course.objects.get(id=id)
    data.delete()
    return redirect('admin_view_course')



def staff_view_attendance(request):
    value_list = Attendance.objects.values_list('date', flat=True).distinct()
    print(value_list)
    attendance = {}
    print(attendance)
    for value in value_list:
        attendance[value] = Attendance.objects.filter(date=value)
        print(attendance[value])
    return render(request, 'teacher_template/staff_view_attendance.html', {'attendances': attendance})

def admin_day_attendance(request,date):
    attendance = Attendance.objects.filter(date=date)
    context = {
        'attendances':attendance,
        'date':date
    }
    return render(request,'admin_template/admin_day_attendance.html',context)




