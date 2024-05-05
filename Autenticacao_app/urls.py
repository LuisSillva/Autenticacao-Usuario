from django.urls import path
from autenticacao_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('cadastro/', views.user_cadastro, name='cadastro'),
    path('home', views.home, name='home'),
    path('signout', views.user_signout, name='signout'),
    path('envia_email/', views.envia_email, name='envia_email'),
    path('password_change', views.password_change, name='password_change'),
    
    # path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    # path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
