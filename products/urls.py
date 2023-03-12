from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.ProductsView.as_view()),
    path("products/<str:product_id>/", views.ProductsDetailView.as_view()),
]
