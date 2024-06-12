from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.root, name='root'),
    path('log-in', auth_views.LoginView.as_view(template_name='log-in.html'), name='log-in'),
    path('home', views.Home.as_view(), name='home'),
    path('sign-up', views.SignUp.as_view(), name='sign-up'),
    path('log-out', views.log_out, name='log-out')
]

