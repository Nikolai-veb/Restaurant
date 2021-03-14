from django.urls import path

from . import views

urlpatterns = [
    path('', views.RecipeListView.as_view(), name='recipe_list'),
    path('single_post/<slug:rec_slug>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('tag/<slug:tag_slug>', views.RecipeListView.as_view(), name='tag_recipe_list'),
    path('category/<slug:cat_slug>/', views.RecipeListView.as_view(), name='category_recipe_list'),
    path("comment/<int:pk>/", views.AddComment.as_view(), name='add_comment'),

]