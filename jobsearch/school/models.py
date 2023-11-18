from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=200, null=True, blank=True)
    course_number = models.IntegerField(null=False)

    def __str__(self):
        return self.course_name

class Student(models.Model):
    name = models.CharField(max_length=200, null=False, blank=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class StudentProfile(models.Model):
    student = models.OneToOneField(Student, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.student)


class Teacher(models.Model):
    name = models.CharField(max_length=200, null=False)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Semester(models.Model):
    semester_no = models.IntegerField(null=False)
    teacher = models.ForeignKey(Teacher, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.semester_no)


class CourseSemester(models.Model):
    course_id = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)
    semester_id = models.ForeignKey(Semester, null=False, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return str(self.start_date)


@receiver(post_save, sender=Student)
def create_student_profile(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'studentprofile'):
        StudentProfile.objects.create(student=instance)