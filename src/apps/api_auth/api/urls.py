from django.urls import path
from .views import MyObtainTokenPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
]