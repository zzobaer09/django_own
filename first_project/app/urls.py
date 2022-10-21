from django.urls import path
from . import views


# ! path for app page

urlpatterns = [
    path("" , views.home , name="home"),

    # * all start routes are going to be right here
    path("list/" , views.list , name="list"),
    # path("list/create/" , views.create , name="create"),
    path("list/<str:name>/" , views.view_data , name="view_item"), #view item form database
    
]



