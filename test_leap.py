import unittest
from leap import checkLeap

class leap_test(unittest.TestCase):
    def test1(self):
        res = checkLeap(1000)
        self.assertEqual(res, False)

    def test2(self):
        res = checkLeap(2000)
        self.assertEqual(res, True)

    def test3(self):
        res = checkLeap(2020)
        self.assertEqual(res, True)


if __name__ == "__main__":
    #0: nothing
    #1: default setting, shows .F
    #2: Shows details - which cases are okay and which cases are failed
    unittest.main(verbosity=2)

    
