from urllib import request
from django.shortcuts import render,redirect
from ch7.models import Item
# Create your views here.


def home_page(request):
       if(request.method=="POST"):
              
              to_do_text=request.POST.get("to_do_name",'')
              Item.objects.create(to_do_list_value=to_do_text)
              #return    render(request,"home1.html",{"a_new_item":to_do_text})4
              return redirect('/lists/the_only_list')
       items=Item.objects.all()
      
       return render(request,"home1.html",{"items":items})
