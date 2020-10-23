# Built-in packages

# Third-party packages
from django.contrib import admin
from django.urls import path

# Local packages

urlpatterns = [
    path("admin/", admin.site.urls),
]
