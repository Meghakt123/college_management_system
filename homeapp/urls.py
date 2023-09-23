from django.urls import path

from homeapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('Course',views.course,name='Course'),
    path('teacher',views.Teachers,name='teacher'),
    path('add_course',views.add_course,name='add_course'),
    path('course_update/<int:id>',views.course_update,name='course_update'),
    path('course_delete/<int:id>',views.course_delete,name='course_delete'),
    path('teacher_registration',views.teacher_registration,name='teacher_registration'),
    path('teacher_update/<int:id>',views.teacher_update,name='teacher_update'),
    path('teacher_delete/<int:id>',views.teacher_delete,name='teacher_delete'),
    path('login_view',views.Login_view,name='login_view'),
    path('register_page',views.register_page,name='register_page'),
    path('student', views.Student, name='student'),
    path('student_delete/<int:id>',views.student_delete,name='student_delete'),
    path('student_dashboard',views.Student_dashboard,name='student_dashboard'),
    path('teacher_dashboard',views.Teacher_dashboard,name='teacher_dashboard'),
    path('profile_view',views.profile_page,name='profile_view'),
    path('attendance_page',views.Attendance_page,name='attendance_page'),
    path('add_attendance/<int:id>',views.Add_attendance,name='add_attendance'),
    path('view_attendance',views.View_attendance,name='view_attendance'),
    path('day_attendance/<date>',views.Day_attendance,name='day_attendance'),
    path('add_notification',views.add_notification,name='add_notification'),
    path('view_notification',views.view_notification,name='view_notification'),
    path('index',views.index,name='index'),
    path('admin_view_notification',views.admin_view_notification,name='admin_view_notification'),
    path('admin_view_course',views.admin_view_course,name='admin_view_course'),
    path('staff_view_attendance',views.staff_view_attendance,name='staff_view_attendance'),
    path('admin_day_attendance/<date>',views.admin_day_attendance,name='admin_day_attendance'),
    path('admin_course_update/<int:id>', views.admin_course_update, name='admin_course_update'),
    path('admin_course_delete/<int:id>', views.admin_course_delete, name='admin_course_delete'),

]