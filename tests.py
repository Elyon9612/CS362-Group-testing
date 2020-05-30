from task import conv_num
import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        test_num = '12345'
        self.assertEqual(12345, conv_num(test_num))
   
    def test2(self):
        test_num = '123.45'
        self.assertEqual(123.45, conv_num(test_num))

    def test3(self):
        test_num = '.45'
        self.assertEqual(0.45, conv_num(test_num))

    def test4(self):
        test_num = '0xAD4'
        self.assertEqual(2772, conv_num(test_num))
       
    
if __name__ == "__main__":
    unittest.main()
