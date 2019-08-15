from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from presentes.views.home import home
from rest_framework.authtoken.views import obtain_auth_token

from presentes.views.perfiles import PerfilViewSet
from presentes.views.casos import CasoViewSet
from presentes.views.organizaciones import OrganizacionViewSet
from presentes.views.provincias import ProvinciaViewSet
from presentes.views.categorias import CategoriaViewSet
from presentes.views.etiquetas import EtiquetaViewSet
from presentes.views.estados_de_caso import EstadoDeCasoViewSet
from presentes.views.estudios import EstudioViewSet
from presentes.views.my_custom_auth import my_obtain_auth_token

router = routers.DefaultRouter(trailing_slash=False)

router.register("perfiles", PerfilViewSet)
router.register("casos", CasoViewSet)
router.register("organizaciones", OrganizacionViewSet)
router.register("provincias", ProvinciaViewSet)
router.register("categorias", CategoriaViewSet)
router.register("etiquetas", EtiquetaViewSet)
router.register("estados-de-caso", EstadoDeCasoViewSet)
router.register("estudios", EstudioViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/auth/', my_obtain_auth_token),
    path('api/', include(router.urls))
]
