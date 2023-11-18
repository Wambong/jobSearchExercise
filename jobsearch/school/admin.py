from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Student)
admin.site.register(StudentProfile)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Semester)
admin.site.register(CourseSemester)
