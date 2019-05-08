from rest_framework.test import APITestCase
from presentes.tests import utilidades

class APIOrganizacionTests(APITestCase):

    def test_puede_listar_los_organizaciones(self):
        utilidades.autenticar(self.client)
        response = self.client.get('/api/organizaciones')
        self.assertEqual(len(response.data['results']), 0)
