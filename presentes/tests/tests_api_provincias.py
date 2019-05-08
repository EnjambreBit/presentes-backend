from rest_framework.test import APITestCase
from presentes.tests import utilidades

class APIProvinciaTests(APITestCase):

    def test_puede_listar_los_provincias(self):
        utilidades.autenticar(self.client)
        response = self.client.get('/api/provincias')
        self.assertEqual(len(response.data['results']), 0)
