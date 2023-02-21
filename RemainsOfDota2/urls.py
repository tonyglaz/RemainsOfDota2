from django.contrib import admin
from django.urls import path
import teams.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',views.hello),
    path('player/',views.PlayerView.as_view()),
    path('player/<int:pk>/',views.PlayerDetailView.as_view()),
]
