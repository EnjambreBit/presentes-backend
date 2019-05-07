from rest_framework.test import APITestCase
from aplicacion.tests import utilidades

class APIModeloTests(APITestCase):

    def test_puede_listar_los_modelo_plural(self):
        utilidades.autenticar(self.client)
        response = self.client.get('/api/modelo_plural')
        self.assertEqual(len(response.data['results']), 0)
