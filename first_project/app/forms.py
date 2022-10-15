from django import forms


class ToDoForm(forms.Form):
    name = forms.CharField(max_length=255 , label="Name")
    items = forms.CharField(max_length=255 , label="Item")
    complete = forms.BooleanField(label="Complete")

    