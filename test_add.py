import unittest


def add(x,y):
    return x + y

class Testadd(unittest.TestCase):

    def test_add(self):
        rest1 = add(1,1)
        self.assertEqual(2,rest1)

    def test_add1(self):
        rest2 = add(1,0)
        self.assertEqual(1,rest2)

    def test_add2(self):
        rest3 = add(-1,2)
        self.assertEqual(1,rest3)

    def test_add3(self):
        test_data = [(1,1,2),(1,0,1),(-1,2,1)]
        for x,y,z in test_data:
            rest4 = add(x,y)
            self.assertEqual(z,rest4)


if __name__ == '__main__':
    unittest.main()