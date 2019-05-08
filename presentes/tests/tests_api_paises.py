from rest_framework.test import APITestCase
from presentes.tests import utilidades

class APIPaisTests(APITestCase):

    def test_puede_listar_los_paises(self):
        utilidades.autenticar(self.client)
        response = self.client.get('/api/paises')
        self.assertEqual(len(response.data['results']), 0)
