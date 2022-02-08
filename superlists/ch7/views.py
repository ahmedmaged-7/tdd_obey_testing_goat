from urllib import request
from django.shortcuts import render,redirect
from ch7.models import Item,List
# Create your views here.


def home_page(request):
    
      
       return render(request,"home2.html")



def new_list(request):
             list_ = List.objects.create()
             to_do_text=request.POST.get("to_do_name",'') 
             Item.objects.create(to_do_list_value=to_do_text,list=list_)
             return redirect(f'/lists/{list_.id}/')


def view_list(request,list_id):
          list_=List.objects.get(id=list_id)
          return render(request,"list.html",{'list_of_items':list_})




def add_item(request,list_id):
             list_=List.objects.get(id=list_id)
             to_do_text=request.POST.get("to_do_name",'')
             
             Item.objects.create(to_do_list_value=to_do_text,list=list_)
             return redirect(f'/lists/{list_id}/')
