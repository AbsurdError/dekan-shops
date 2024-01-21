from django.db import models

# Create your models here.
class Item_Notebook(models.Model):
    title = models.TextField()
    price = models.CharField(max_length=30)
    path_img = models.TextField()

    def __str__(self):
        return self.title

class Item_Comp_Mouse(models.Model):
    title = models.TextField()
    price = models.CharField(max_length=30)
    path_img = models.TextField()

    def __str__(self):
        return self.title

class Item_Headphones(models.Model):
    title = models.TextField()
    price = models.CharField(max_length=30)
    path_img = models.TextField()

    def __str__(self):
        return self.title
