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
        
    def test5(self):
        test_num = '-0xFF'
        self.assertEqual(conv_num(test_num), -255)      
    
    def test6(self):
        test_num = '12345A'
        self.assertEqual(conv_num(test_num), None)

    def test7(self):
        test_num = '12.3.45'
        self.assertEqual(conv_num(test_num), None)
        
    def test8(self):
        test_num = ''
        self.assertEqual(conv_num(test_num), None)

    def test9(self):
        test_num = '-'
        self.assertEqual(conv_num(test_num), None)

    def test10(self):
        test_num = '1.'
        self.assertEqual(conv_num(test_num), 1.)

    def test11(self):
        test_num = '.1'
        self.assertEqual(conv_num(test_num), .1)

    def test12(self):
        test_num = '0x'
        self.assertEqual(conv_num(test_num), None)

    def test13(self):
        test_num = '-0x'
        self.assertEqual(conv_num(test_num), None)

        
if __name__ == "__main__":
    unittest.main()
