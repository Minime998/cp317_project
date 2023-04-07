import unittest
from IMC import IMC


class TestIMC(unittest.TestCase):

    def test_run(self):
        recipe = []
        self.assertEqual(IMC(recipe), None, "should have finished")


if __name__ == '__main__':
    unittest.main()
