from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm
app_name = 'Loginify'

urlpatterns =[
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logoutView, name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='Loginify/login.html', authentication_form=LoginForm), name='login'), ]

