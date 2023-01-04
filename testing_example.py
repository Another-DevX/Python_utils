import unittest


def sum(number_1, number_2):
    return number_1 + number_2

class ExampleTest(unittest.TestCase):
    def test_failure(self):
        """Test_failure
        if result is'nt 20, test failure
        """
        result = sum(12,10)
        
        self.assertEqual(result, 20)
        
    def test_ok(self):
        """Test_pass
        if result is 20, test pass
        """
        result = sum(10,10)
        self.assertEqual(result, 20)
        
if __name__ == '__main__':
     unittest.main()