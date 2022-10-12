from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList , Item
# Create your views here.



# ! OBJECT FROM DB
ls = ToDoList.objects



# ! here i have created two views



# * home page
def home(response):
    return HttpResponse(render(response , "app/home.html" , {}))


def list(response):
    list_ = [i.name for i in ls.all()]
    return HttpResponse(render(response , "app/list.html",{"ls":list_}))


def log_in(response):
    return render(response , "app/log_in.html" , {})

###############################

def view_data(response , name):
    __name = ls.get(name=name)
    __todo = __name.item_set.all()

    return HttpResponse(render(response , "app/list_item.html", {"name":__name , "todo":__todo}))
