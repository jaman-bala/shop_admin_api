from django.urls import path
from backend.apps import views

urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    path("product/<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
    path("products/", views.ProductListView.as_view(), name="product_list"),
    path("products/<str:category_slug>/", views.ProductListView.as_view(), name="category_list"),
    path("products/<str:category_slug>/<str:subcategory_slug>/",
         views.ProductListView.as_view(),
         name="subcategory_list"
         )

]