from rest_framework.test import APITestCase
from presentes.tests import utilidades

class APICasoTests(APITestCase):

    def test_puede_listar_los_casos(self):
        utilidades.autenticar(self.client)
        response = self.client.get('/api/casos')
        self.assertEqual(len(response.data['results']), 0)
