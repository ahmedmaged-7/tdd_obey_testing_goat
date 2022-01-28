from urllib import request
from django.shortcuts import render
from ch5.models import Item
# Create your views here.


def home_page(request):
       to_Do_item=Item()
       to_Do_item.to_do_list_value=request.POST.get("item_text",'')
       to_Do_item.save()
       if(request.method=="POST"):
           return    render(request,"home1.html",{"a_new_item":request.POST["to_do_name"],})
       return render(request,"home1.html")
