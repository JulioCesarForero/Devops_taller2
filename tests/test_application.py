import unittest
from application import application

class TestApplication(unittest.TestCase):

    def setUp(self):
        # Configurar la aplicación para pruebas
        self.app = application.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'A-Bomb', response.data)  # Verificar que uno de los héroes está en la respuesta

    def test_heroe(self):
        response = self.app.get('/0')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'"name": "A-Bomb"', response.data)  # Verificar que el héroe con ID '0' se devuelve correctamente

    def test_heroe_not_found(self):
        response = self.app.get('/999')
        self.assertEqual(response.status_code, 500)  # Esto dependerá de cómo manejes los errores en la aplicación

if __name__ == '__main__':
    unittest.main()

