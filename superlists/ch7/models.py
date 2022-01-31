from django.db import models

# Create your models here.

class Item(models.Model):
     to_do_list_value=models.TextField(default= '')#remmeber to add a default
    
