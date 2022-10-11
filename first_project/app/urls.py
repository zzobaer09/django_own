from django.urls import path
from . import views


# ! path for app page

urlpatterns = [
    path("" , views.index , name="index"),

    # * all start routes are going to be right here
    path("start/" , views.v1 , name="v1"),
    path("start/<str:name>/" , views.view_data , name="view data from database"),
    
    # * routes of log_in
    path("log_in/" , views.log_in , name="log in page"),
]