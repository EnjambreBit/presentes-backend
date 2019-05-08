from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from presentes.views.home import home
from rest_framework.authtoken.views import obtain_auth_token

from presentes.views.perfiles import PerfilViewSet

router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    # path('api/auth/', my_obtain_auth_token),
    path('api/', include(router.urls))
]
