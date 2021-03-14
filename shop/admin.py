from django.contrib import admin

from .models import Categories, Tags, Products, Comments


@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    list_display_links = ("id", "name")
    list_filter = ("name",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Tags)
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
    list_filter = ("name", "description", "category", "create", "price", "tags")
    search_fields = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "parent", "product", "moderation")
    list_display_links = ("id", "name")
    list_filter = ("name", "parent")
    list_editable = ("moderation",)
    search_fields = ("name", "text", "email")
