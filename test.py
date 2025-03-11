import unittest
import houses_API

class TestAPICalls(unittest.TestCase):
    def _sold_function(self):
        properties = []
        houses_API.Sold(properties)
        if len(properties) > 0:
            return True
        else:
            return False
        
    def test_Sold(self):
       self.assertTrue(self._sold_function())

if __name__  == '__main__':
    unittest.main()
