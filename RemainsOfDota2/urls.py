from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

import teams.views as views

router = routers.SimpleRouter()
router.register('team', views.TeamViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('hello/', views.hello),
    path('player/', include('teams.urls'))
]

urlpatterns += router.urls
