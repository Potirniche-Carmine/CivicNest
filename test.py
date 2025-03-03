import unittest
import houses_API

class TestAPICalls(unittest.TestCase):
    def _for_sale_function(self):
        properties = []
        houses_API.ForSale(properties)
        if len(properties) > 0:
            return True
        else:
            return False
            
    def _for_rent_function(self):
        properties = []
        houses_API.ForRent(properties)
        if len(properties) > 0:
            return True
        else:
            return False

    def _sold_function(self):
        properties = []
        houses_API.Sold(properties)
        if len(properties) > 0:
            return True
        else:
            return False
        
    def test_ForSale(self):
        self.assertTrue(self._for_sale_function())

    def test_ForRent(self):
        self.assertTrue(self._for_rent_function())
    
    def test_Sold(self):
        self.assertTrue(self._sold_function())

if __name__  == '__main__':
    unittest.main()
