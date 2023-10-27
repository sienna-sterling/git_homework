import myProgram
import unittest

class TestEven(unittest.TestCase):
    def test_six(self):
        self.assertEqual(myProgram.isEven(9), True)

if __name__ == '__main__':
    unittest.main()