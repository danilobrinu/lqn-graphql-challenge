# Built-in packages

# Third-party packages
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

# Local packages
from .common import *  # noqa skipcq: PYL-W0614

urlpatterns += [
    path("graphql/", csrf_exempt(GraphQLView.as_view())),
]
