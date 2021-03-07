from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name='home'),
    path("menu/", views.MenuListView.as_view(), name='list_menu'),

]