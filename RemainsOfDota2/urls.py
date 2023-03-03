from django.contrib import admin
from django.urls import path, include

import teams.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/',include('rest_framework.urls')),
    path('hello/', views.hello),
    path('player/', include('teams.urls'))
]
