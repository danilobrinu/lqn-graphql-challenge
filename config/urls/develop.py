# Built-in packages

# Third-party packages
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

# Local packages
# skipcq: PYL-W0614
from config.urls.common import *  # noqa
from api_v1.schema import schema as api_v1_schema

urlpatterns += [
    path("graphql/v1", csrf_exempt(GraphQLView.as_view(schema=api_v1_schema))),
    path("graphiql/v1", csrf_exempt(GraphQLView.as_view(schema=api_v1_schema, graphiql=True))),
]
