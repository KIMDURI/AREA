from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.language, name = 'language'),
    path('result/', views.result, name = 'test'),
    path('test/', views.quiz, name = 'quiz'),
]

