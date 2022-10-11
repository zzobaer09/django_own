from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList , Item
# Create your views here.

# ! here i have created two views

def index(response):
    return HttpResponse("""<h1>first django project</h1>
                            <h2>you come to home</h2>""")


def v1(response):
    return HttpResponse("<h1>this is another page</h1>")


def log_in(response):
    return HttpResponse("""
                            <h1> you have to log in to continue </h1>
                            <button>click here to log in</button>
                            """)


###############################
ls = ToDoList

def view_data(response , name):
    __name = ls.objects.get(name=name)
    __todo = __name.item_set.all()

    r = ""
    for i in __todo:
        r += "<p>%s</p>" %i.text

    return HttpResponse(""" 
                            <h1>%s</h1> 
                            <br>
                            <br>
                            <p>%s</p>
                            
                        """ %(__name.name , r))
