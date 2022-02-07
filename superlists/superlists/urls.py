"""superlists URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from ch3 import views
from ch5 import views as views_ch5
from ch7 import views as views_ch7
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'',views.home_page,name='home')  #do not forget to add ,
    url(r'^$',views_ch7.home_page),
    url(r'^lists/the_only_list/$',views_ch7.view_list),
    url(r'^lists/new',views_ch7.new_list)

]
