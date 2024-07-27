from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("", include("user_side.urls")),
    path("accounts/", include("accounts.urls")),
    path("administration/", include("administration.urls"))
]
