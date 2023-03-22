from django.db import models

class Menu(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=200)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

class SubCategory(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
