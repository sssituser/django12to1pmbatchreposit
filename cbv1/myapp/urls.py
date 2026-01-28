from django.urls import path
from myapp.views import HelloView

urlpatterns=[
    path('',HelloView.as_view()),
]