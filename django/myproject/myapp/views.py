from django.shortcuts import render,HttpResponse
from django.views import View
import json




#TODO FBV
def users(request):
    user_list = ['ldz','goodboys']
    return HttpResponse(json.dumps(user_list))


class StudentsView(View):
    def get(self,request,*args,**kwargs):
        return HttpResponse("GET")
    def post(self,request,*args,**kwargs):
        return HttpResponse("POST")
    def put(self,request,*args,**kwargs):
        return HttpResponse("PUT")
    def delete(self,request,*args,**kwargs):
        return HttpResponse("DELETE")



