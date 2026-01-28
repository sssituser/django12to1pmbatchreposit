from django.urls import path
from myapp import views

urlpatterns=[
    path('',views.AddProduct.as_view()),
    path('list/',views.ProductList.as_view(),name='list'),
    
]