from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from .views import base_views, email_auth
from rest_framework.authtoken.views import obtain_auth_token

app_name = "users"

urlpatterns = [
    path("signup/", base_views.SignUpView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('activate/<str:uid>/<str:token>',
         email_auth.UserActivateView.as_view(), name='activate'),
    path('login/', base_views.LoginView.as_view(), name='login'),
    path('retrieve/', base_views.UserInfoView.as_view(), name='retrieve'),
]