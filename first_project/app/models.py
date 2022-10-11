from django.db import models

# Create your models here.


class ToDoList(models.Model):
    name = models.CharField(max_length = 255)
    def __str__(self) -> str:
        return self.name

class Item(models.Model):
    todolist = models.ForeignKey(ToDoList , on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    complete = models.BooleanField()

    def __str__(self) -> str:
        return self.text

        