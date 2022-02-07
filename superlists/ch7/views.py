from urllib import request
from django.shortcuts import render,redirect
from ch7.models import Item,List
# Create your views here.


def home_page(request):
       if(request.method=="POST"):
              list_=List.objects.create()
              to_do_text=request.POST.get("to_do_name",'')
              Item.objects.create(to_do_list_value=to_do_text,list=list_)
              #return    render(request,"home1.html",{"a_new_item":to_do_text})4
              return redirect('/lists/the_only_list/')
      
       return render(request,"home1.html")



def view_list(request):
       if(request.method=="POST"):
              list_=List.objects.create()
              to_do_text=request.POST.get("to_do_name",'')
              Item.objects.create(to_do_list_value=to_do_text,list=list_)
              #return    render(request,"home1.html",{"a_new_item":to_do_text})4
              return redirect('/lists/the_only_list/')
       items=Item.objects.all()
       return render(request,"list.html",{"items":items})



def new_list(request):
              list_=List.objects.create()
              Item.objects.create(to_do_list_value=request.POST.get("item_text",''),list=list_)
              return redirect('/lists/the_only_list/')#make sure what you passed in test and html value as 

