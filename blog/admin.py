from django.contrib import admin

from .models import Categories, Tags, Recipes, Comments


@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    list_display_links = ("id", "name")
    list_filter = ("name",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    list_display_links = ("id", "name")
    list_filter = ("name",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Recipes)
class RecipesAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "create", "moderation", "get_image")
    list_display_links = ("id", "title")
    list_filter = ("title", "tags", "category")
    list_editable = ("moderation",)
    search_fields = ("title", "text")
    prepopulated_fields = {"slug": ("title", "tags")}


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "parent", "recipe", "moderation")
    list_display_links = ("id", "name")
    list_filter = ("name", "parent")
    list_editable = ("moderation",)
    search_fields = ("name", "text", "email")
