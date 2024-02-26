from django.urls import path
from Autenticacao_app import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('cadastro/', views.user_cadastro, name='cadastro'),
    path('home', views.home, name='home'),
]
