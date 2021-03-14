from django.urls import path

from . import views


urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('product/<slug:prod_slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('product_tag/<slug:tag_slug>/', views.ProductListView.as_view(), name='product_tag'),
    path('product/<slug:cat_slug>/', views.ProductListView.as_view(), name='product_cat'),
    path("comment/<int:pk>/", views.AddComment.as_view(), name='add_comment'),
]