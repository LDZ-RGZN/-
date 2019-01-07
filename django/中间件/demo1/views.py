from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

EXCLUDE_IPS = ['127.0.0.1']

# def forbidden_ip(view_func):
#     def wrapper(request,*args,**kwargs):
#         user_ip = request.META['REMOTE_ADDR']
#         if user_ip in EXCLUDE_IPS:
#             return HttpResponse("<h1>禁止访问</h1>")
#         else:
#             return view_func(request,*args,**kwargs)
#     return wrapper


# @forbidden_ip
def index(request):
    return HttpResponse("成功!")



"""
EXCLUDE_IPS = ['127.0.0.1']

def index(request):
    user_ip = request.META['REMOTE_ADDR']
    if user_ip in EXCLUDE_IPS:
        return HttpResponse("<h1>禁止访问</h1>")
    return HttpResponse("你好!")
"""