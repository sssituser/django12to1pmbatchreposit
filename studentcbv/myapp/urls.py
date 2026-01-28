from django.urls import path
from myapp.views import *

urlpatterns=[
    path('',StudentList.as_view(),name='list'),
    path('create/',CreateStudent.as_view()),
    path('<int:pk>/',StudentDetails.as_view()),
    path('edit/<int:pk>/',UpdateStudent.as_view()),
    path('delete/<int:pk>/',DeleteStudent.as_view()),
]