from django.urls import path
from myapp import views


urlpatterns = [
    path('', views.students, name='student_list'), 
    path('register/', views.register, name='create_student'),
    
]