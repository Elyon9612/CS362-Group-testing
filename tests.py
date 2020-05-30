import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        test_num = '12345'
        self.assertEqual(12345, conv_num(test_num))


if __name__ == "__main__":
    unittest.main()
