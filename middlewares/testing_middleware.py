from demo_middleware.models import Newstats
from django.db.models import F


class DummyMiddleware():
    
    def __init__(self, get_response):
        self.get_response = get_response
        self.num_request = 0
        self.num_exception = 0

    def stats(self, os_info):
        if "Windows" in os_info:
            Newstats.objects.all().update(win=F('win') + 1)
        elif "mac" in os_info:
            Newstats.objects.all().update(mac=F('mac') + 1)
        elif "iPhone" in os_info:
            Newstats.objects.all().update(iph=F('iph') + 1)
        elif "Android" in os_info:
            Newstats.objects.all().update(android=F('android') + 1)
        else:
            Newstats.objects.all().update(oth=F('oth') + 1)


    def __call__(self, request):
        
        self.num_request += 1
        print(f"Requests handle so far : {self.num_request}")
        print(request.META['HTTP_USER_AGENT'])
        if "admin" not in request.path:
            self.stats(request.META['HTTP_USER_AGENT'])
        response = self.get_response(request)

        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        # Logic executed before a call to view
        # Gives the access to the view itself and arguments
        print(f"view name : {view_func.__name__}")
        # pass

    def process_exception(self, request, exception):
        self.num_exception += 1
        print(f"Exception count : {self.num_exception}")
        pass

    # def process_template_response(request, response):
    #     pass