# Built-in packages

# Third-party packages
from django.views.decorators.csrf import csrf_exempt

# Local packages
from .common import *

urlpatterns += [
    path("graphql/", csrf_exempt(GraphQLView.as_view())),
    path("graphiql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]

