from django.http import HttpResponse
class SecondClassMiddleware(object):
    def __init__(self,get_response):
        print('Init Method from SecondClass Middleware')
        self.get_response = get_response


    def __call__(self,request):
        print('pre request in SecondClass Middleware')
        response=self.get_response(request)
        print('post request in SecondClass Middleware')
        return response