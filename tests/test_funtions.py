import unittest
from funtions import load_file

class TestFunctions(unittest.TestCase):

    def setUp(self):
        # Se ejecuta antes de cada prueba
        self.file_name = 'heroes.csv'

    def test_load_file(self):
        data = load_file(self.file_name)
        self.assertIsInstance(data, dict)  # Verificar que el resultado sea un diccionario
        self.assertIn('0', data)  # Verificar que el ID '0' esté presente en los datos cargados
        self.assertEqual(data['0']['name'], 'A-Bomb')  # Verificar que el nombre del ID '0' sea 'A-Bomb'

    def test_load_file_no_file(self):
        # Prueba que se produzca un error cuando el archivo no existe
        with self.assertRaises(FileNotFoundError):
            load_file('no_existe.csv')

if __name__ == '__main__':
    unittest.main()
