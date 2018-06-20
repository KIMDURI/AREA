from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import login, logout
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('chat/', include('chat.urls')),
    path('quiz/', include('quiz.urls')),
    path('board/', include('board.urls')),

    path('login/', auth_views.login, name='login'),
    path('join/', views.join, name='join'),
    path('logout/', auth_views.logout, {'next_page' : '/'}, name='logout'),

    path('admin/', admin.site.urls),
]

