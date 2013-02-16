from __future__ import unicode_literals

from django_nose import FastFixtureTestCase as TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from accounts import forms


class UserFormTest(TestCase):
    def setUp(self):
        # User
        self.user = User()
        self.user.username = 'test_username'
        self.user_form = forms.UserForm(instance=self.user)

    def tearDown(self):
        pass

    def test_clean_username_new(self):
        """
        Test when it's a new username
        """
        self.user_form.data = {'username': 'test_username'}
        self.assertEquals(
            'test_username', self.user_form.clean_username())

    def test_clean_username_error(self):
        """
        Test when the username exists
        """
        user = User.objects.create_user(
            'test', 'test@email.com', 'password')
        user.username = 'test_username2'
        user.save()
        
        self.user_form.data = {'username': 'test_username2'}
        with self.assertRaises(ValidationError) as cm:
            self.user_form.clean_username()
            
        the_exception = cm.exception
        self.assertEqual(the_exception.messages, ['The username '\
                '"test_username2" is already taken'])
