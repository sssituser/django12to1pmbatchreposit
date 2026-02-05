from django.http import HttpResponse
class ErrorMessageMiddleWare(object):
    def __init__(self,get_response):
        print("Init method in exception middleware")
        self.get_response = get_response
    def __call__(self,request):
        print('pre request middleware exception')
        response=self.get_response(request)
        print('post request middleware exception')
        return response
    def process_exception(self,request,exception):
        return HttpResponse(f'<h1>Currently we are facing Technical problem try after some time : {exception}</h1>')

        
