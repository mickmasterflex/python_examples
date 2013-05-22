from __future__ import unicode_literals

from django_nose import FastFixtureTestCase as TestCase
from django.contrib.auth.models import User

from accounts import constants
from accounts import models


class ModelsModuleTest(TestCase):
    fixtures = ['test_user_data']

    def setUp(self):
        self.user = User.objects.get(pk=1)

    def tearDown(self):
        pass

    def test_get_profile_create(self):
        profile = models._get_profile(self.user)
        self.assertIsNotNone(profile.id)
        self.assertEqual(profile.user, self.user)

    def test_get_profile_get(self):
        profile = models.UserProfile.objects.create(user=self.user)
        profile_get = models._get_profile(self.user)
        self.assertEqual(profile_get, profile)

    def test_user_profile_get(self):
        self.assertIsInstance(self.user.profile, models.UserProfile)


class UserProfileTest(TestCase):
    def setUp(self):
        # User
        self.user = User()
        self.user.username = 'test'
        self.user.first_name = 'Test'
        self.user.last_name = 'Example'
        self.user.is_active = True
        self.user.is_staff = True
        self.user_is_superuser = False

        # UserProfile
        self.user_profile = models.UserProfile()
        self.user_profile.user = self.user
        self.user_profile.permission = 'ses_staff'

    def tearDown(self):
        pass

    def test_unicode(self):
        self.assertEqual('Test Example\'s Profile',
                unicode(self.user_profile))
        self.user.last_name = None
        self.assertEqual('Test\'s Profile', unicode(self.user_profile))
        self.user.first_name = None
        self.assertEqual('test\'s Profile', unicode(self.user_profile))

    def test_is_active(self):
        self.assertTrue(self.user_profile.is_active)
        user = User()
        user.is_active = False
        self.user_profile.user = user
        self.assertFalse(self.user_profile.is_active)

    def test_is_staff(self):
        self.assertTrue(self.user_profile.is_staff)
        user = User()
        user.is_staff = False
        self.user_profile.user = user
        self.assertFalse(self.user_profile.is_staff)

    def test_is_permitted_staff_not_permitted(self):
        self.assertFalse(self.user_profile.is_permitted(['ses_admin']))

    def test_is_permitted_is_superuser(self):
        self.user.is_superuser = True
        self.assertTrue(self.user_profile.is_permitted(['ses_admin']))

    def test_is_permitted_staff_permitted(self):
        self.assertTrue(self.user_profile.is_permitted(['ses_staff']))

    def test_set_django_permissions(self):
        self.user.save()
        self.user_profile.user = self.user
        self.user_profile.permission = constants.PERMISSION_PARTNER
        self.user_profile.save()
        self.assertEqual(self.user.is_staff, False)
        self.user_profile.permission = constants.PERMISSION_ADMIN
        self.user_profile.save()
        self.assertEqual(self.user.is_staff, True)
        self.assertEqual(self.user.is_superuser, False)
