from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from presentes.views.home import home
from rest_framework.authtoken.views import obtain_auth_token

from presentes.views.perfiles import PerfilViewSet
from presentes.views.casos import CasoViewSet
from presentes.views.my_custom_auth import my_obtain_auth_token

router = routers.DefaultRouter(trailing_slash=False)

router.register("perfiles", PerfilViewSet)
router.register("casos", CasoViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/auth/', my_obtain_auth_token),
    path('api/', include(router.urls))
]
