from django.contrib import admin

from .models import Categories, Status, Products


@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    list_display_links = ("id", "name")
    list_filter = ("name",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    list_display_links = ("id", "name")
    list_filter = ("name",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "moderation", "get_image")
    list_editable = ("moderation",)
    list_display_links = ("id", "name")
    list_filter = ("name", "description", "category", "status", "create", "price")
    search_fields = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}
