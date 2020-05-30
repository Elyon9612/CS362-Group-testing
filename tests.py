from task import conv_num
import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        test_num = '12345'
        self.assertTrue(conv_num(test_num), 12345)

if __name__ == "__main__":
    unittest.main()
