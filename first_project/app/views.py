from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList , Item
from .forms import ToDoForm

# Create your views here.



# ! OBJECT FROM DB
# global variable !!!!!!!!! do not touch it
ls = ToDoList.objects



# ! here i have created two views



# * home page
def home(response):
    return HttpResponse(render(response , "app/home.html" , {}))


def list(response):
    list_ = ls.all()

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
            return HttpResponseRedirect("{}/".format(t.name))

        # delete ToDoList
        for i in list_:
            if response.POST.get("d{}".format(i.id)) == "delete":
                i.delete()
                
    else:
        create_form = ToDoForm()

    return HttpResponse(render(response , "app/list.html",{"ls": list_ , "FORM": create_form}))


def log_in(response):
    return render(response , "app/log_in.html" , {})

###############################

def view_data(response , name):
    __name = ls.get(name=name)
    __item_set = __name.item_set
    __todo = __item_set.all()

    if response.method == "POST":
        # print(response.POST)
        if response.POST.get("d{}".format(__name.id)) == "delete":
            __name.delete()
            return HttpResponseRedirect("/list/")

        if response.POST.get("save"):

            # to add item in ToDoList
            if response.POST.get("newItemField"):
                txt = response.POST.get("newItemField")
                __item_set.create(text=txt , complete=False)

            # to check mark and delete an item
            elif response.POST.get("save"):
                # check uncheck
                for item in __todo:
                    if response.POST.get("c{}".format(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()
                    # delete item
                    if response.POST.get("d{}".format((item.id))) == "delete":
                        item.delete()


    return HttpResponse(render(response , "app/list_item.html", {"name":__name , "todo":__todo}))



# def create(response):

#     if response.method == "POST":
#         create_form = ToDoForm(response.POST)
#         if create_form.is_valid():

#             # all value
#             _name = create_form.cleaned_data["name"]
#             _item = create_form.cleaned_data["items"]
#             _complete = create_form.cleaned_data["complete"]

#             """
#                 database work
#             """

#             t = ToDoList(name=_name)
#             t.save()
#             t.item_set.create(text=_item , complete=_complete)
#             return HttpResponseRedirect("../{}/".format(t.name))

#     else:
#         create_form = ToDoForm()
#     return HttpResponse(render(response , "app/create.html" , {"FORM":create_form}))























    