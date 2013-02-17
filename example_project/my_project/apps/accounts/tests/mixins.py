from django.core.exceptions import PermissionDenied
from django.http import HttpRequest, HttpResponseRedirect
from django.test.utils import override_settings
from django_nose import FastFixtureTestCase as TestCase

from accounts import mixins


class MockRequest(object):
    def __init__(self):
        self.user = MockUser()


class MockUser(object):
    is_authenticated_return = True

    def __init__(self):
        self.profile = MockProfile()

    def is_authenticated(self):
        return MockUser.is_authenticated_return


class MockProfile(object):
    is_permitted_return = True
    is_permitted_params = []

    def is_permitted(self, permissions):
        MockProfile.is_permitted_params.append({'permissions': permissions})
        return MockProfile.is_permitted_return


@mixins.permissions_required(['admin'])
def admin_view(request):
    pass


class MockView(object):
    dispatch_params = []

    def dispatch(self, request, *args, **kwargs):
        MockView.dispatch_params.append(
            {'request': request, 'args': args, 'kwargs': kwargs})
        return 'dispatch result'


class AdminAuthenticationView(mixins.LoginRequiredMixin, MockView):
    pass


class AdminPermissionView(mixins.PermissionsRequiredMixin, MockView):
    permissions_required = ['admin']


class MixinsModuleTest(TestCase):
    def setUp(self):
        self.request = MockRequest()
        MockProfile.is_permitted_return = True
        MockProfile.is_permitted_params = []

    def tearDown(self):
        pass

    def test_permissions_required_raise_permission_denied(self):
        MockProfile.is_permitted_return = False
        with self.assertRaises(PermissionDenied):
            admin_view(self.request)
        self.assertEqual(MockProfile.is_permitted_params,
                         [{'permissions': ['admin']}])

    def test_permissions_required(self):
        try:
            admin_view(self.request)
        except PermissionDenied, e:
            self.fail('Did not expect PermissionDenied to be raised.')
        self.assertEqual(MockProfile.is_permitted_params,
                         [{'permissions': ['admin']}])


class LoginRequiredMixinTest(TestCase):
    def setUp(self):
        self.request = HttpRequest()
        self.request.user = MockUser()
        self.request.META = {'SERVER_NAME': 'localhost', 'SERVER_PORT': 8000}
        MockUser.is_authenticated_return = True
        self.admin_view = AdminAuthenticationView()
        MockView.dispatch_params = []

    def tearDown(self):
        pass

    @override_settings(LOGIN_URL='/login/')
    def test_dispatch_redirect(self):
        MockUser.is_authenticated_return = False
        response = self.admin_view.dispatch(self.request, 'arg', kwarg='value')
        self.assertIsInstance(response, HttpResponseRedirect)
        self.assertEqual(response['Location'], '/login/?next=')
        self.assertEqual(MockView.dispatch_params, [])

    def test_dispatch(self):
        try:
            result = self.admin_view.dispatch(
                self.request, 'arg', kwarg='value')
        except PermissionDenied, e:
            self.fail('Did not expect PermissionDenied to be raised.')
        self.assertEqual(result, 'dispatch result')
        self.assertEqual(
            MockView.dispatch_params,
            [{
                'request': self.request, 'args': ('arg',),
                'kwargs': {'kwarg': 'value'}
            }])


class PermissionsRequiredMixinTest(TestCase):
    def setUp(self):
        self.request = MockRequest()
        MockProfile.is_permitted_return = True
        MockProfile.is_permitted_params = []
        self.admin_view = AdminPermissionView()
        MockView.dispatch_params = []

    def tearDown(self):
        pass

    def test_dispatch_raise_permission_denied(self):
        MockProfile.is_permitted_return = False
        with self.assertRaises(PermissionDenied):
            self.admin_view.dispatch(self.request, 'arg', kwarg='value')
        self.assertEqual(MockProfile.is_permitted_params,
                         [{'permissions': ['admin']}])
        self.assertEqual(MockView.dispatch_params, [])

    def test_dispatch(self):
        try:
            result = self.admin_view.dispatch(
                self.request, 'arg', kwarg='value')
        except PermissionDenied, e:
            self.fail('Did not expect PermissionDenied to be raised.')
        self.assertEqual(result, 'dispatch result')
        self.assertEqual(MockProfile.is_permitted_params,
                         [{'permissions': ['admin']}])
        self.assertEqual(
            MockView.dispatch_params,
            [{
                'request': self.request, 'args': ('arg',),
                'kwargs': {'kwarg': 'value'}
            }])

