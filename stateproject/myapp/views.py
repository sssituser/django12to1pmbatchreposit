from django.shortcuts import render

# Create your views here.
def home_view(request):
    print('Cookies from the client:',request.COOKIES)
    count = int(request.COOKIES.get('count',0))
    count += 1
    response = render(request,'myapp/Home.html',{'count':count})
    response.set_cookie('count',count)
    return response

    #request.COOKIES.get('ckname',ckvalue)
    #response.set_cookie('ckname',ckvalue) // In order to store the cookie 