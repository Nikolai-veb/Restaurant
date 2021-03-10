from django.contrib import admin

from .models import Categories, Images


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    list_display_links = ("id", "name")
    list_filter = ("name",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "moderation", "get_image")
    list_display_links = ("id", "name")
    list_filter = ("name",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    list_editable = ("moderation",)
