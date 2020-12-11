import  unittest

ABD = 0
from login import username,userpassword


class TestLogin(unittest.TestCase):

    def test_login_username(self):
        expect_username = 'chen'

        acutl_username = username()
        self.assertEqual(expect_username,acutl_username)

        # assert expect_username == acutl_username
    @unittest.skipIf(ABD>1,'cuowu')
    def test_login_userpassword(self):
        expect_password = 'test01'
        acutl_password = userpassword()
        self.assertEquals(expect_password,acutl_password)
        # assert expect_password == acutl_password


suite = unittest.TestSuite()

# suite.addTest(TestLogin('test_login_username'))
# suite.addTest(TestLogin('test_login_userpassword'))

suite = unittest.TestLoader().discover('.',pattern='test*.py')

runner = unittest.TextTestRunner()
runner.run(suite)