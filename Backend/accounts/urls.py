from . import views
from django.urls import path


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path("signup/",views.SignupView.as_view(),name="signup"),
    path("login/", views.LoginView.as_view(), name="login"),
    path('jwt/create/', views.Mytoken_view.as_view(), name='token_obtain_pair'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),
]