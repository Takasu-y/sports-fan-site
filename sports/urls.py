from django.urls import path
from . import views

app_name='sports'

urlpatterns = [
    path('', views.index, name='index'),
    path('rules/<str:pk>/', views.rules, name='rules'),
    path('notables/<str:pk>/', views.notables, name='notables'),
    path('links/<str:pk>/', views.links, name='links'),
]
