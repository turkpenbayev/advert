from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self,):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self,):
        return self.name


class Advert(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='adverts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='adverts')
    views = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self,):
        return self.title
