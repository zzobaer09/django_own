from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList , Item
from .forms import ToDoForm
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



def create(response):

    if response.method == "POST":
        create_form = ToDoForm(response.POST)
        if create_form.is_valid():

            # all value
            _name = create_form.cleaned_data["name"]
            _item = create_form.cleaned_data["items"]
            _complete = create_form.cleaned_data["complete"]

            """
                database work
            """

            t = ToDoList(name=_name)
            t.save()
            t.item_set.create(text=_item , complete=_complete)
            return HttpResponseRedirect("../{}/".format(t.name))

    else:
        create_form = ToDoForm()
    return HttpResponse(render(response , "app/create.html" , {"FORM":create_form}))























    