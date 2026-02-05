
from django.http import HttpResponse
# Create your views here.
def home(request):
    
    return HttpResponse(f"<h1>Hi Iam Home Function {10/0}</h1>",)
    