
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *


from .models import *


def home(request):
    teachers = Teacher.objects.all()
    courses = Course.objects.all()
    teacher_name = request.GET.get('teacher_name', '')
    course_name = request.GET.get('course_name', '')

    combined_data = StudentProfile.objects.select_related(
        'student__course', 'student__course__coursesemester', 'student__course__coursesemester__semester',
        'student__course__coursesemester__semester__teacher'
    ).filter(
        student__course__coursesemester__semester_id__teacher__name__icontains=teacher_name,
        student__course__course_name__icontains=course_name
    ).values(
        'student__id', 'student__name', 'student__first_name',
        'student__course__course_name', 'student__course__course_number',
        'student__course__coursesemester__semester_id__semester_no',
        'student__course__coursesemester__start_date', 'student__course__coursesemester__end_date',
        'student__course__coursesemester__semester_id__teacher__name',
    )

    content = {
        "teachers": teachers,
        "courses": courses,
        "combined_data": combined_data,
        "teacher_name": teacher_name,
        "course_name": course_name,
    }
    return render(request, 'index.html', content)

def add_course(request):
    courses = Course.objects.all()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_course')
    else:
        form = CourseForm()

    return render(request, 'add_course.html', {'form': form, "courses":courses})

def add_student(request):
    students = Student.objects.all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_student')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form, "students":students})

def add_teacher(request):
    teachers = Teacher.objects.all()
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_teacher')
    else:
        form = TeacherForm()
    return render(request, 'add_teacher.html', {'form': form, "teachers":teachers})


def add_coursesemester(request):
    course_semesters = CourseSemester.objects.all()
    if request.method == 'POST':
        form = CourseSemesterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_coursesemester')
    else:
        form = CourseSemesterForm()
    return render(request, 'add_coursesemester.html', {'form': form,  'course_semesters': course_semesters})


def add_semester(request):
    semesters = Semester.objects.all()
    if request.method == 'POST':
        form = SemesterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_semester')
    else:
        form = SemesterForm()
    return render(request, 'add_semester.html', {'form': form, "semesters":semesters})


def update_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm(instance=student)

    return render(request, 'update_student.html', {'form': form, 'student': student})


def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    if request.method == 'POST':
        student.delete()
        return redirect('home')

    return render(request, 'delete_student.html', {'student': student})

def update_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CourseForm(instance=course)

    return render(request, 'update_course.html', {'form': form, 'course': course})


def delete_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    if request.method == 'POST':
        course.delete()
        return redirect('home')

    return render(request, 'delete_course.html', {'course': course})

def update_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)

    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TeacherForm(instance=teacher)

    return render(request, 'update_teacher.html', {'form': form, 'teacher': teacher})


def delete_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)

    if request.method == 'POST':
        teacher.delete()
        return redirect('home')

    return render(request, 'delete_teacher.html', {'teacher': teacher})

# semester update and delete

def update_semester(request, semester_id):
    semester = get_object_or_404(Semester, pk=semester_id)

    if request.method == 'POST':
        form = SemesterForm(request.POST, instance=semester)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SemesterForm(instance=semester)

    return render(request, 'update_semester.html', {'form': form, 'semester': semester})


def delete_semester(request, semester_id):
    semester = get_object_or_404(Semester, pk=semester_id)

    if request.method == 'POST':
        semester.delete()
        return redirect('home')

    return render(request, 'delete_semester.html', {'semester': semester})

# course update and delete
def update_coursesemester(request, course_semester_id):
    course_semester = get_object_or_404(CourseSemester, pk=course_semester_id)
    if request.method == 'POST':
        form = CourseSemesterForm(request.POST, instance=course_semester)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CourseSemesterForm(instance=course_semester)

    return render(request, 'update_coursesemester.html', {'form': form, 'course_semester': course_semester})


def delete_coursesemester(request, course_semester_id):
    course_semester = get_object_or_404(CourseSemester, pk=course_semester_id)

    if request.method == 'POST':
        course_semester.delete()
        return redirect('home')

    return render(request, 'delete_coursesemester.html', {'course_semester': course_semester})

