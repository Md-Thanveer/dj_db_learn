from django.contrib import admin
from .models import Teacher, TeacherProfile, Course, Student, Department, Enrollment

admin.site.register(Teacher)
admin.site.register(TeacherProfile)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Enrollment)