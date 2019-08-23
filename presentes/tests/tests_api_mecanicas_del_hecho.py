from rest_framework.test import APITestCase
from presentes.tests import utilidades

class APIMecanicaDelHechoTests(APITestCase):

    def test_puede_listar_los_mecanicas_del_hecho(self):
        utilidades.autenticar(self.client)
        response = self.client.get('/api/mecanicas_del_hecho')
        self.assertEqual(len(response.data['results']), 0)
