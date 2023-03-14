from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("users/", views.UserView.as_view()),
    path("users/<str:user_id>/", views.UserDetailView.as_view()),
    path("orders/", views.UserOrderView.as_view()),
    path("orders/user/", views.ListOrders.as_view()),
    path("orders/product/list/", views.ListProductsOrdered.as_view()),
    path("orders/<str:order_id>/", views.UserOrderUpdate.as_view()),
    path("login/", TokenObtainPairView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
]
