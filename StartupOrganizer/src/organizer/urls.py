from django.urls import path

# from .views import hello_world #Using base view function
from .views import HelloWorld  # Using class base views

urlpatterns = [
    # if request match the path ""
    # then past the request to the hello_world view
    # and we are naming this path "hello"
    # path("", hello_world, name="hello")#Using base view function
    path("", HelloWorld.as_view(), name="hello")  # Using base class view
]
