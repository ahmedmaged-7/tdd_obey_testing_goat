
from django.conf.urls import url
from ch7 import views as views_ch7


urlpatterns = [

 url(r'^(\d+)/add_item/',views_ch7.add_item),
    url(r'^(\d+)/',views_ch7.view_list),#when i used the terrible "(./)" mad million error
    url(r'^new/',views_ch7.new_list),
]

