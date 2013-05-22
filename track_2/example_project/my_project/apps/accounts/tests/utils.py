from django_nose import FastFixtureTestCase as TestCase
from django.contrib.auth.models import User

from accounts import utils


class UtilsTest(TestCase):
    def setUp(self):
        # User
        self.user = User.objects.create_user(
            'test', 'test@email.com', 'password')
        self.user.username = 'test_username_is_valid'
        self.user.save()
        
    def tearDown(self):
        pass

    def test_is_username_valid(self):
        """
        Test when the username exists
        """
        username = 'test_username_is_valid'
        self.assertFalse(utils.is_username_valid(username))

        username = 'test_username_is_valid2'
        self.assertTrue(utils.is_username_valid(username))
