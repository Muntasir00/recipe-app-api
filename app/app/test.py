"""Sample Test"""

from django.test import SimpleTestCase


from app import calc


class CalcTest(SimpleTestCase):
    def testAdd(self):
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def testsub(self):
        res = calc.subtract(10, 15)
        self.assertEqual(res, 5)
