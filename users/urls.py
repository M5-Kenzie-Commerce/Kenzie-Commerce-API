from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.UserView.as_view()),
    path("users/", views.UserDetailView.as_view()),
]