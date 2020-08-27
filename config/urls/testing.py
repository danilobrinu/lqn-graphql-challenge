from .common import *

urlpatterns += [
    path("graphql/", csrf_exempt(GraphQLView.as_view())),
]

