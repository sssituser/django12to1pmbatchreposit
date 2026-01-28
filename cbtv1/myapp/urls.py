#from django.urls import path
# from myapp import views
# urlpatterns=[
#     path('',views.Home.as_view()),
#     path('register/',views.Register.as_view()),
#     path('login/',views.Login.as_view()),
# ]

from django.urls import path
from myapp.views import *

urlpatterns =[
    path('',Home.as_view()),
    path('register/',Register.as_view()),
    path('login/',Login.as_view()),
]