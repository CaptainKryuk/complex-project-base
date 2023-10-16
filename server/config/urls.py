from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .schema import schema

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/api/', include('users.api.urls')),

    path('graphql/', GraphQLView.as_view(graphiql=True, schema=schema))
]
