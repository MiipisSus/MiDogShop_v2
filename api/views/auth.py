from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.utils import extend_schema_view, extend_schema

@extend_schema_view(
    post=extend_schema(tags=["auth"], summary="Obtain JWT token")
    )
class CustomTokenObtainPairView(TokenObtainPairView):
    pass

@extend_schema_view(
    post=extend_schema(tags=["auth"], summary="Refresh JWT token")
    )
class CustomTokenRefreshView(TokenRefreshView):
    pass