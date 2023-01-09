import unittest

class CajaNegraTest(unittest.TestCase):
    
    def test_sum(self):
        num1 = 10
        num_2 = 5
        
        resultado = suma(num1, num_2)
        
        self.assertDictEqual(resultado, 15)
    
if __name__ == '__main__':
    unittest.main()