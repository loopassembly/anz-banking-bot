from django.urls import path
from django.conf.urls import url
from . import views
from django.views.static import serve 
from django.conf import settings
urlpatterns = [
    path("",views.home,name="get_name"),
    path("get",views.get_bot_response,name="get_bot_response"),
   
    
    
    
]