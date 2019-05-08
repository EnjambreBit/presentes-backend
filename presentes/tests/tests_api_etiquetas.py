from rest_framework.test import APITestCase
from presentes.tests import utilidades

class APIEtiquetaTests(APITestCase):

    def test_puede_listar_los_etiquetas(self):
        utilidades.autenticar(self.client)
        response = self.client.get('/api/etiquetas')
        self.assertEqual(len(response.data['results']), 0)
