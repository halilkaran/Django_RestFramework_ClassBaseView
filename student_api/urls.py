from django.urls import path,include
from .views import (
    home,
    student_api,
    student_api_get_update_delete,
    path_api,
    StudentList,
    StudentDetaill,
    StudentListCreate,
    StudentUpDe,
    StudentLC,
    StudentRUD,
    StudentGRUD,
    student_create_api,
    student_delete_api,
    student_list_api,
    student_partial_udate,
    student_update_api
)

from rest_framework import routers

router = routers.DefaultRouter()
router.register('students', StudentGRUD)

urlpatterns = [
    path('', home),
    # path('student/', student_api),
   # path('student/', StudentList.as_view()),
    #path('student/<int:pk>/', student_api_get_update_delete, name="detail"),
    #path('student/<int:pk>/', StudentDetaill.as_view(), name="detail"),
   # path('path/', path_api),
    # path('student_list', student_list_api),
    # path('student_create', student_create_api),
    #path('student/', StudentListCreate.as_view()),
    #path('student/', StudentLC.as_view()),
    #path('student/<int:pk>/', StudentUpDe.as_view()),
    #path('student/<int:pk>/', StudentRUD.as_view()),
    # path('student_update/<int:pk>', student_update_api),
    # path('student_delete/<int:pk>', student_delete_api),
    # path('student_patch/<int:pk>', student_partial_udate),
    path('', include(router.urls))
]
