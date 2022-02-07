from django.db import models

# Create your models here.
class List(models.Model):
     pass


class Item(models.Model):
     to_do_list_value=models.TextField(default= '')#remmeber to add a default
     list=models.ForeignKey(List,default=None)
