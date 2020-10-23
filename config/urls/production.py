# Built-in packages

# Third-party packages
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

# Local packages
# skipcq: PYL-W0614
from .common import *  # noqa

urlpatterns += [
    path("graphql/", csrf_exempt(GraphQLView.as_view())),
]
