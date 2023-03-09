from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("users/", views.UserView.as_view()),
    path("users/<str:user_id>/", views.UserDetailView.as_view()),
    path("oders/", views.UserOrderView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
]
