from accounts.views import (AccountChangePasswordView,
                            AccountCreateView,
                            AccountLoginView,
                            AccountLogoutView,
                            AccountUpdateView)

from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('register/', AccountCreateView.as_view(), name='register'),
    path('login/', AccountLoginView.as_view(), name='login'),
    path('profile/', AccountUpdateView.as_view(), name='profile'),
    path('logout/', AccountLogoutView.as_view(), name='logout'),
    path('password/', AccountChangePasswordView.as_view(), name='password'),
]