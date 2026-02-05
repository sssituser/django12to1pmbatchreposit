from django.http import HttpResponse

# class AppMaintenceMiddleware(object):
#     def __init__(self,get_response):
#         self.get_response = get_response

#     def __call__(self,request):
#         response = self.get_response(request)
#         return HttpResponse('<h1>Currently application under maintenance … Please try  after 2 days </h1>')

class FirstClassMiddleware(object):
    def __init__(self,get_response):
        print('Init method in First Class')
        self.get_response = get_response

    def __call__(self,request):
        print('preprocess Request in First Class')
        response = self.get_response(request)
        print('Post process Request in First Class')
        return response