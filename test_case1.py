from login import username,userpassword



def test_login_username():
    expect_username = 'chen'

    acutl_username = username()
    assert expect_username == acutl_username


def test_login_userpassword():
    expect_password = 'test01'
    acutl_password = userpassword()
    assert expect_password == acutl_password


test_login_username()
test_login_userpassword()