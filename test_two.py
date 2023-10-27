import myProgram
import unittest

class TestSum(unittest.TestCase):
    def test_char(self):
        with self.assertRaises(TypeError):
            myProgram.isEven("a")

if __name__ == '__main__':
    unittest.main()