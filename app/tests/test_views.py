"""test user authentication"""
import unittest
import json
from app import create_app

class Testusers(unittest.TestCase):
    """ Tests for user  """
    def setUp(self):
        """setup"""

        app = create_app(config_name='testing')
        self.client = app.test_client()

        self.register_user = json.dumps({
            "username": "simon",
            "email" :"awitimon23@gmail.com",
            "password":'Pass123',
            "userRole":'client',
            "confirmpass":'Pass123'})

        self.register_user2 = json.dumps(dict(
            username = "kenneth",
            email = "kkkisimon23@gmail.com",
            password='Pass123',
            userRole='client',
            confirmpass='Pass123'))

        self.register_user3 = json.dumps(dict(
            username = "john",
            email = "bbbbimon23@gmail.com",
            password='Pass123',
            userRole='client',
            confirmpass='Pass123'))

        self.client.post(
            '/api/v1/auth/sign up',
            data=self.register_user,
            content_type='application/json')

        self.client.post(
            '/api/v1/auth/sign up',
            data=self.register_user2,
            content_type='application/json')


    def test_registration(self):
        """Test for user registration"""
        resource = self.client.post(
            '/api/v1/auth/sign up',
            data=json.dumps(dict(
                username = "felix",
                email = "bbrfn23@gmail.com",
                password='Pa123',
                userRole='client',
                confirmpass='pa123')), content_type='application/json')
        data = json.loads(resource.data.decode())
        self.assertEqual(resource.status_code, 201)
        self.assertEqual(resource.content_type, 'application/json')
        self.assertEqual(data['message'].strip(), 'Signup Successful')


    def test_username_already_taken(self):
        """ Test if username already taken """
        resource = self.client.post(
            '/api/v1/auth/sign up',
            data=json.dumps(dict(
                username = "john",
                email = "bbbbimon23@gmail.com",
                password='Pass123',
                userRole='client',
                confirmpass='pass123')), content_type='application/json')
        data = json.loads(resource.data.decode())
        self.assertEqual(resource.status_code, 400)
        self.assertEqual(resource.content_type, 'application/json')
        self.assertEqual(data['message'].strip(), 'Username is taken.')


    def test_login(self):
        """ Test login """
        self.client.post(
            '/api/v1/auth/login',
            data=json.dumps(dict(
                username = "john",
                email = "bbbbimon23@gmail.com",
                password='Pass123',
                userRole='client',
                confirmpass='pass123')), content_type='application/json')
        resource = self.client.post(
            '/v2/users/login',
            data=json.dumps(dict(username="john", password='Pass123')),
            content_type='application/json')
        data = json.loads(resource.data.decode())
        self.assertEqual(resource.status_code, 200)
        self.assertEqual(resource.content_type, 'application/json')
        self.assertEqual(
            data['message'].strip(),
            'You are successfully logged in')


    def test_wrong_login_username(self):
        """ Test login validation """
        resource = self.client.post(
            '/api/v1/auth/login',
            data=json.dumps(dict(username="joseph", password='Pass12')),
            content_type='application/json')
        data = json.loads(resource.data.decode())
        self.assertEqual(resource.status_code, 401)
        self.assertEqual(resource.content_type, 'application/json')
        self.assertEqual(data['message'].strip(), 'Please register first.')


    def test_wrong_login_password(self):
        """ Test wrong login password """
        self.client.post(
            '/api/v1/auth/login',
            data=json.dumps(dict(
                username="user1",
                userphone='0712991490',
                password='Pass123',
                userRole='client',
                confirmpass='Pass123')), content_type='application/json')
        resource = self.client.post(
            '/v2/auth/login',
            data=json.dumps(dict(username="user1", password='12')),
            content_type='application/json')
        data = json.loads(resource.data.decode())
        self.assertEqual(resource.status_code, 403)
        self.assertEqual(resource.content_type, 'application/json')
        self.assertEqual(data['message'].strip(), 'Wrong username or password')

if __name__ == '__main__':
    unittest.main()