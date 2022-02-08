from urllib import request
from django.shortcuts import render,redirect
from ch7.models import Item,List
# Create your views here.


def home_page(request):
       if(request.method=="POST"):
              list_=List.objects.create()
              Item.objects.create(to_do_list_value=request.POST.get("to_do_name",''),list=list_)
              return redirect(f'/lists/{list_.id}/')
      
       return render(request,"home1.html")



def view_list(request,list_id):
          if(request.method=="POST"):
              print(f"triggered with id {list_id}")         
              list_=List.objects.create()
              to_do_text=request.POST.get("to_do_name",'')
              Item.objects.create(to_do_list_value=to_do_text,list=list_)
              return redirect(f'/lists/{list_id}/')
          list_=List.objects.get(id=list_id)
          items=Item.objects.filter(list=list_)
          return render(request,"list.html",{"items":items})




def new_list(request):
              list_=List.objects.create()
              Item.objects.create(to_do_list_value=request.POST.get("to_do_name",''),list=list_)
              return redirect(f'/lists/{list_.id}/')#make sure what you passed in test and html value as 

