from django_nose import FastFixtureTestCase as TestCase
from django import template
from django.template import base as template_base

from accounts.templatetags import permissions
from accounts.tests import mocks


permissions.constants = mocks.constants


class MockUser(object):
    @property
    def profile(self):
        return MockUserProfile()


class MockUserProfile(object):
    is_permitted_params = []
    is_permitted_return = True

    def is_permitted(self, permissions):
        MockUserProfile.is_permitted_params.append(
            {'permissions': permissions})
        return MockUserProfile.is_permitted_return


class MockParser(object):
    parse_params = []
    delete_first_token_called = False

    def __init__(self, next_token):
        self._next_token = next_token

    def parse(self, parse_until=None):
        MockParser.parse_params.append({'parse_until': parse_until})
        return 'nodelist'

    def next_token(self):
        return self._next_token

    def delete_first_token(self):
        MockParser.delete_first_token_called = True


class MockToken(object):
    def __init__(self, split_contents_return, contents):
        self.split_contents_return = split_contents_return
        self.contents = contents

    def split_contents(self):
        return self.split_contents_return


class MockNodeList(object):
    def __init__(self):
        self.render_params = []

    def render(self, context):
        self.render_params.append({'context': context})
        return 'rendered'


class IfPermittedNodeTest(TestCase):
    def setUp(self):
        self.permission_constant = 'PERMISSIONS_TEST'
        self.nodelist_true = MockNodeList()
        self.nodelist_false = MockNodeList()
        self.if_permitted_node = permissions.IfPermittedNode(
            self.permission_constant, self.nodelist_true, self.nodelist_false)
        MockUserProfile.is_permitted_params = []
        MockUserProfile.is_permitted_return = True

    def tearDown(self):
        pass

    def test_init_missing_constant(self):
        with self.assertRaises(ValueError):
            permissions.IfPermittedNode(
                'INVALID_CONSTANT', self.nodelist_true, self.nodelist_false)

    def test_init_constant_not_iter(self):
        if_permitted_node = permissions.IfPermittedNode(
            'PERMISSION_TEST_STRING', self.nodelist_true, self.nodelist_false)
        self.assertEqual(if_permitted_node.permissions, ['perm1'])

    def test_init(self):
        self.assertEqual(self.if_permitted_node.permissions,
                         ['perm1', 'perm2'])
        self.assertIs(self.if_permitted_node.nodelist_true,
                         self.nodelist_true)
        self.assertIs(self.if_permitted_node.nodelist_false,
                         self.nodelist_false)

    def test_render_is_permitted(self):
        context = {'user': MockUser()}
        self.if_permitted_node.render(context)
        self.assertEqual(MockUserProfile.is_permitted_params,
                         [{'permissions': ['perm1', 'perm2']}])
        self.assertEqual(self.nodelist_true.render_params,
                         [{'context': context}])
        self.assertEqual(self.nodelist_false.render_params, [])

    def test_render_is_not_permitted(self):
        MockUserProfile.is_permitted_return = False
        context = {'user': MockUser()}
        self.if_permitted_node.render(context)
        self.assertEqual(MockUserProfile.is_permitted_params,
                         [{'permissions': ['perm1', 'perm2']}])
        self.assertEqual(self.nodelist_true.render_params, [])
        self.assertEqual(self.nodelist_false.render_params,
                         [{'context': context}])


class ModulesTest(TestCase):
    def setUp(self):
        self.token = MockToken(['ifpermitted', 'PERMISSIONS_TEST'],
                               'ifpermitted')
        self.next_token = MockToken([], 'ifpermitted')
        self.parser = MockParser(self.next_token)
        MockParser.parse_params = []
        MockParser.delete_first_token_called = False

    def tearDown(self):
        pass

    def test_ifpermitted_token_split_contents_1(self):
        token = MockToken(['ifpermitted'], 'ifpermitted')
        with self.assertRaises(template.TemplateSyntaxError):
            permissions.ifpermitted(self.parser, token)

    def test_ifpermitted_token_split_contents_3(self):
        token = MockToken(['ifpermitted', 'PERMISSIONS_TEST', 'other'],
                          'ifpermitted')
        with self.assertRaises(template.TemplateSyntaxError):
            permissions.ifpermitted(self.parser, token)

    def test_ifpermitted_with_else(self):
        next_token = MockToken(['ifpermitted', 'PERMISSIONS_TEST'], 'else')
        parser = MockParser(next_token)
        if_permitted_node = permissions.ifpermitted(parser, self.token)
        self.assertIsInstance(if_permitted_node, permissions.IfPermittedNode)
        self.assertEqual(
            MockParser.parse_params,
            [
                {'parse_until': ('else', 'endifpermitted')},
                {'parse_until': ('endifpermitted',)}
            ])
        self.assertTrue(MockParser.delete_first_token_called)
        self.assertEqual(if_permitted_node.permissions, ['perm1', 'perm2'])
        self.assertEqual(if_permitted_node.nodelist_true, 'nodelist')
        self.assertEqual(if_permitted_node.nodelist_false, 'nodelist')

    def test_ifpermitted_without_else(self):
        if_permitted_node = permissions.ifpermitted(self.parser, self.token)
        self.assertIsInstance(if_permitted_node, permissions.IfPermittedNode)
        self.assertEqual(
            MockParser.parse_params,
            [{'parse_until': ('else', 'endifpermitted')}])
        self.assertFalse(MockParser.delete_first_token_called)
        self.assertEqual(if_permitted_node.permissions, ['perm1', 'perm2'])
        self.assertEqual(if_permitted_node.nodelist_true, 'nodelist')
        self.assertIsInstance(if_permitted_node.nodelist_false,
                              template_base.NodeList)

