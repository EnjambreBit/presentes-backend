from rest_framework.test import APITestCase
from presentes.tests import utilidades

class APIPerfilTests(APITestCase):

    def test_puede_listar_los_perfiles(self):
        utilidades.autenticar(self.client)
        response = self.client.get('/api/perfiles')
        self.assertEqual(len(response.data['results']), 0)
