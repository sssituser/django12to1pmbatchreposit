from django.http import HttpResponse
class FirstClassMiddleware(object):
    def __init__(self,get_response):
        print('Init Method from FirstClass Middleware')
        self.get_response = get_response


    def __call__(self,request):
        print('pre request in FirstClass Middleware')
        response=self.get_response(request)
        print('post request in FirstClass Middleware')
        return response