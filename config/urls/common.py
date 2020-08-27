# Built-in packages

# Third-party packages
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

# Local packages

urlpatterns = [
    path("admin/", admin.site.urls),
]
