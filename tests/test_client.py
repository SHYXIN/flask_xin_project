import re
import unittest
from app import create_app, db
from app.models import User, Role

class FlaskClientTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        Role.insert_roles()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        # self.assertTrue(b'陌生人' in response.data)
        self.assertTrue('陌生人' in response.get_data(as_text=True))

    def test_register_and_login(self):
        # register a new account
        response = self.client.post('/auth/register', data={
            'email': 'john@example.com',
            'username': 'john',
            'password': 'cat',
            'password2': 'cat'
        })
        self.assertEqual(response.status_code, 302)

        # login with the new account
        response = self.client.post('/auth/login', data={
            'email': 'john@example.com',
            'password': 'cat'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        # self.assertTrue(re.search(b'Hello,\s+john!', response.data))
        self.assertTrue(re.search('你好，\s+john', response.get_data(as_text=True)))
        # self.assertTrue(
        #     b'You have not confirmed your account yet' in response.data)
        self.assertTrue(
            '您尚未确认您的账户' in response.get_data(as_text=True)
        )


        # send a confirmation token
        user = User.query.filter_by(email='john@example.com').first()
        token = user.generate_confirmation_token()
        response = self.client.get('/auth/confirm/{}'.format(token),
                                   follow_redirects=True)
        user.confirm(token)
        self.assertEqual(response.status_code, 200)
        # self.assertTrue(
        #     b'You have confirmed your account' in response.data)
        self.assertTrue(
            '您已确认您的帐户' in response.get_data(
                as_text=True
            )
        )

        # log out
        response = self.client.get('/auth/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        # self.assertTrue(b'You have been logged out' in response.data)
        self.assertTrue('您已退出登录' in response.get_data(
            as_text=True
        ))
