from urllib import request
from django.shortcuts import render

# Create your views here.


def home_page(request):
     """
     return render(request,"home1.html",{
            "a_new_item":request.POST.get("to_do_name",''),#dict.get if confused
                       })

     """  
     if(request.method=="POST"):
        print("THIS IS REQUEST VALUE"+str(request)) 
        return    render(request,"home1.html",{"a_new_item":request.POST["to_do_name"],})
     return render(request,"home1.html")