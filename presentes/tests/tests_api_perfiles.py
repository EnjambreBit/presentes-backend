from rest_framework.test import APITestCase
from presentes.tests import utilidades
from django.contrib.auth.models import User
from presentes.models.perfiles import Perfil

class APIPerfilTests(APITestCase):

    def test_puede_listar_los_perfiles_y_obtener_mi_perfil(self):
        utilidades.autenticar(self.client)
        response = self.client.get('/api/perfiles')
        self.assertEqual(len(response.data['results']), 2)

        response = self.client.get('/api/perfiles/mi-perfil')
        self.assertEqual(response.data['permisos']['perfiles.puede_crear'], False)
        self.assertTrue(response.data['version_del_servidor'])
