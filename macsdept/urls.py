from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('approve', views.approve, name='approve'),
    path('postnotice', views.postnotice, name='postnotice')
]
