# Built-in packages

# Third-party packages
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

# Local packages
from .common import *  # noqa

urlpatterns += [
    path("graphql/", csrf_exempt(GraphQLView.as_view())),
    path("graphiql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
