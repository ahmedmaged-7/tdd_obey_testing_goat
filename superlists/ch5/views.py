from urllib import request
from django.shortcuts import render
from ch5.models import Item
# Create your views here.


def home_page(request):
       if(request.method=="POST"):
              to_Do_item=Item()
              to_Do_item.to_do_list_value=request.POST.get("to_do_name",'')
              to_Do_item.save()
              return    render(request,"home1.html",{"a_new_item":to_Do_item.to_do_list_value})
       return render(request,"home1.html")
