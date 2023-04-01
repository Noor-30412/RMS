from django.urls import path
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('booking/', views.booking, name='booking'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('forgot_password/', auth_views.PasswordResetView.as_view(), name='forgot_password'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
