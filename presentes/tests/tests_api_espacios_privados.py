from rest_framework.test import APITestCase
from presentes.tests import utilidades

class APIEspacioPrivadoTests(APITestCase):

    def test_puede_listar_los_espacios_privados(self):
        utilidades.autenticar(self.client)
        response = self.client.get('/api/espacios_privados')
        self.assertEqual(len(response.data['results']), 0)
