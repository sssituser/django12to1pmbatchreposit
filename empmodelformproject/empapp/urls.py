from django.urls import path
from empapp import views
urlpatterns =[
    path('',views.employees,name='emplist'),
    path('register/',views.register,name="add"),
    path('edit/',views.edit,name='edit'),
    path('show/',views.show,name='show'),
    path('del/',views.delete,name='delete'),
]