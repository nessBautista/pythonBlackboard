from django.http import HttpResponse
from django.views import View  # this import allows me to have a class base view


class HelloWorld(View):
    def get(self, request):
        return HttpResponse("hello World from base class view!")


""" Using basic Django View Function
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "HEAD"])
def hello_world(request):
    # return a default status code of 200=ok
    # content type of text html
    # character set using the UTF-8 encoding
    return HttpResponse("Hello World!")
"""
