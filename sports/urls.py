from django.urls import path
from . import views

app_name='sports'

urlpatterns = [
    path('', views.index, name='index'),
    path('rules/<str:pk>/', views.rules, name='rules'),
    path('notables/<int:pk>/', views.notables, name='notables'),
    path('notables/<int:pk>/detail/<str:name>', views.playerDetail, name='player_detail'),
    path('links/<str:pk>/', views.links, name='links'),
]
