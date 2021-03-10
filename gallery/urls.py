from django.urls import path

from . import views

urlpatterns = [
    path('gallery/', views.GalleryListView.as_view(), name='list_gallery'),
]