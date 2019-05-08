from rest_framework.test import APITestCase
from presentes.tests import utilidades

class APICategoriaTests(APITestCase):

    def test_puede_listar_los_categorias(self):
        utilidades.autenticar(self.client)
        response = self.client.get('/api/categorias')
        self.assertEqual(len(response.data['results']), 0)
