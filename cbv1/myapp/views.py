from django.shortcuts import render
from django.views.generic import *

from django.http import HttpResponse
# Create your views here.

# class HelloView(View):
#     def get(self,request):
#         return HttpResponse("<h1>Hi this is the example for view class</h1>")
# class MyView(View):
#     def get(self,request):
#         return render(request,'home.html')
#     def post(self,request):
#         return HttpResponse("<h1> Hi this is POST Method from Myview</h1>")
class HelloView(TemplateView):
    template_name="home.html"
    def post(self,request):
        return HttpResponse("<h1> Hi Iam Post method")