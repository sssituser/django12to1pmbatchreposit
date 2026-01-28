from django.urls import path
from myapp.views import *

urlpatterns=[
    path('',AddEmployee.as_view(),name='create'),
    path('list/',Employees.as_view(),name='list'),
    path('edit/<int:id>/',EditEmployee.as_view(),name='edit'),
    path('delete/<int:id>/',DeleteEmployee.as_view(),name='delete'),
    path('show/<int:id>/',FindEmployee.as_view(),name='find'),
]