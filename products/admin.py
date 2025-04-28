from django.contrib import admin
from .models import Category,Products

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name","slug"]
    prepopulated_fields = {'slug':('name',)}



@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
     list_display = ["name","price","available","created","updated","category"]
     prepopulated_fields = {'slug':('name',)}


