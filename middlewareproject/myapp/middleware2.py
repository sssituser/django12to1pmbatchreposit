class SecondClassMiddleware(object):
    def __init__(self,get_response):
        print('Init method in Second Class')
        self.get_response = get_response

    def __call__(self,request):
        print('preprocess Request in Second Class')
        response = self.get_response(request)
        print('Post process Request in Second Class')
        return response 