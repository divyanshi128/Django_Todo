from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    
    # ======================= AFTER LOGIN ========================
    
    path("dashboard/", views.dashboard, name="dashboard"),
    path("my_profile/", views.my_profile, name="my_profile"),
    path("change_password/", views.change_password, name="change_password"),
    
    path("add_todo/", views.add_todo, name="add_todo"),
    path("delete_todo/<int:id>/", views.delete_todo, name="delete_todo"),
    path("edit_todo/<int:id>/", views.edit_todo, name="edit_todo"),
]
