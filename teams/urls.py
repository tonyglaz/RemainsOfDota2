from django.urls import path
from rest_framework import routers

import teams.views as views

urlpatterns = [
    path('', views.PlayerListView.as_view()),
    path('<int:pk>/', views.PlayerDetailView.as_view()),
    path('create/', views.PlayerCreateView.as_view()),
    path('<int:pk>/update/', views.PlayerUpdateView.as_view()),
    path('<int:pk>/delete/', views.PlayerDeleteView.as_view()),
]

