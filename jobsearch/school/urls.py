from django.urls import path
from .views import *
from .api_views import *

urlpatterns = [
    path('', home, name="home"),
    path('add_course/', add_course, name='add_course'),
    path('add_student/', add_student, name='add_student'),
    path('add_teacher/', add_teacher, name='add_teacher'),
    path('add_coursesemester/', add_coursesemester, name='add_coursesemester'),
    path('add_semester/', add_semester, name='add_semester'),

#    student updates and deletes
    path('update_student/<int:student_id>/', update_student, name='update_student'),
    path('delete_student/<int:student_id>/', delete_student, name='delete_student'),
    # course update and delete
    path('update_course/<int:course_id>/', update_course, name='update_course'),
    path('delete_course/<int:course_id>/', delete_course, name='delete_course'),
#     teacher update and delete
    path('update_teacher/<int:teacher_id>/', update_teacher, name='update_teacher'),
    path('delete_teacher/<int:teacher_id>/', delete_teacher, name='delete_teacher'),
#     semester update and delete
    path('update_semester/<int:semester_id>/', update_semester, name='update_semester'),
    path('delete_semester/<int:semester_id>/', delete_semester, name='delete_semester'),
    # update and delete course semester
    path('update_coursesemester/<int:course_semester_id>/', update_coursesemester, name='update_coursesemester'),
    path('delete_coursesemester/<int:course_semester_id>/', delete_coursesemester, name='delete_coursesemester'),

#  , , Course
#    API URLS
    path('api/students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('api/students/<int:pk>/', StudentRetrieveUpdateDestroyView.as_view(), name='student-retrieve-update-destroy'),

    path('api/teachers/', TeacherListCreateView.as_view(), name='teacher-list-create'),
    path('api/teachers/<int:pk>/', TeacherRetrieveUpdateDestroyView.as_view(), name='teacher-retrieve-update-destroy'),

    path('api/studentprofiles/', StudentProfileListCreateView.as_view(), name='studentprofile-list-create'),
    path('api/studentprofiles/<int:pk>/', StudentProfileRetrieveUpdateDestroyView.as_view(), name='studentprofile-retrieve-update-destroy'),

    path('api/semesters/', SemesterListCreateView.as_view(), name='semester-list-create'),
    path('api/semesters/<int:pk>/', SemesterRetrieveUpdateDestroyView.as_view(), name='semester-retrieve-update-destroy'),

    path('api/coursesemesters/', CourseSemesterListCreateView.as_view(), name='courseSemester-list-create'),
    path('api/coursesemesters/<int:pk>/', CourseSemesterRetrieveUpdateDestroyView.as_view(), name='courseSemester-retrieve-update-destroy'),

    path('api/courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('api/courses/<int:pk>/', CourseRetrieveUpdateDestroyView.as_view(), name='course-retrieve-update-destroy'),
]

