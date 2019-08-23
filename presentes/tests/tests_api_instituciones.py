from rest_framework.test import APITestCase
from presentes.tests import utilidades

class APIInstitucionTests(APITestCase):

    def test_puede_listar_los_instituciones(self):
        utilidades.autenticar(self.client)
        response = self.client.get('/api/instituciones')
        self.assertEqual(len(response.data['results']), 0)
