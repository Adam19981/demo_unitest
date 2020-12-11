from parameterized import parameterized
import unittest



def add(x,y):
    return x + y

test_data = [(1,2,3),(1,0,1),(-1,3,2)]

class Testadd(unittest.TestCase):

    @parameterized.expand(test_data)
    def test_add(self,a,b,c):
        rest = add(a,b)
        self.assertEqual(c,rest)





if __name__ == '__main__':
    unittest.main()