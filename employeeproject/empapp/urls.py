from django.urls import path
from empapp import views

urlpatterns=[
    path('',views.home),
    path('employees/',views.employees),
]