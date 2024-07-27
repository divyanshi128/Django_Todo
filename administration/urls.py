from django.urls import path

from . import views

urlpatterns = [
    path("", views.admin_dashboard, name="admin_dashboard"),
    path("delete_user/<int:user_id>", views.delete_user, name="delete_user"),
]
