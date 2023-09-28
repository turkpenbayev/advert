from django.contrib import admin
from adverts.models import City, Category, Advert


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'views', 'created')
    list_filter = ('city', 'category')
    search_fields = ('title',)
    ordering = ('title', 'city_id')
