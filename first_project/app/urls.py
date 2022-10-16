from django.urls import path
from . import views


# ! path for app page

urlpatterns = [
    path("" , views.home , name="home"),

    # * all start routes are going to be right here
    path("list/" , views.list , name="list"),
    path("list/create/" , views.create , name="create"),
    path("list/<str:name>/" , views.view_data , name="view data from database"),
    
    # * routes of log_in
    path("log_in/" , views.log_in , name="log in page"),
]




"""
# TODO

-make a base template
-inherit base to the home template
-list (list/) template -> inherit form base(this page will show the all name of database)
-list (list/<str:name>/) -> inherit form base or list (this page will show the all items in database)                               

"""