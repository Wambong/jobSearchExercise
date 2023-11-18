# forms.py
from django import forms
from .models import Course, Student, Teacher, Semester, CourseSemester


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'course_number']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'first_name', 'course']


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'first_name', 'title']


class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = ['semester_no', 'teacher']


class CourseSemesterForm(forms.ModelForm):
    class Meta:
        model = CourseSemester
        fields = ['course_id', 'semester_id', 'start_date', 'end_date']
