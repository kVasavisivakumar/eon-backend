from django.urls import path
from .views import Login, Register, change_user_password
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('login', Login.as_view(), name='login'),
    path('registration', Register.as_view(), name='registration'),
    path('token-refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('change-password', change_user_password)
]