from collections import namedtuple
from ftw.builder import Builder
from ftw.builder import create
from ftw.table.helper import linked
from ftw.table.helper import linked_without_icon
from ftw.table.testing import FTWTABLE_INTEGRATION_TESTING
from ftw.table.utils import IS_PLONE_5
from lxml.html import fromstring
from plone.app.testing import login
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from Products.CMFCore.Expression import Expression
from Products.CMFCore.utils import getToolByName
from unittest import skipIf
from unittest import TestCase


class TestLinkedWithIcon(TestCase):

    layer = FTWTABLE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        login(self.portal, TEST_USER_NAME)

        self.folder = create(Builder('folder').titled(
            u'the <"escaped"> Title').having(
            description=u'a <"f\xc3\xa4ncy"> description',
            ))

        self.brain = getToolByName(self.portal, 'portal_catalog')(
            portal_type="Folder")[0]

    def test_has_link_if_called_with_a_brain(self):
        html = fromstring(linked(self.brain, self.brain.Title))

        self.assertEqual('a', html.find('a').tag)

    def test_has_link_with_obj(self):
        html = fromstring(linked(self.folder, self.folder.Title()))

        self.assertEqual('a', html.find('a').tag)

    @skipIf(IS_PLONE_5, 'Plone 5 no longer uses "icon_exp"')
    def test_has_img_tag_in_link_tag(self):
        self.folder.getTypeInfo().icon_expr_object = Expression(
            'string:folder.jpg')
        self.folder.reindexObject()
        self.brain = getToolByName(self.portal, 'portal_catalog')(
            portal_type="Folder")[0]
        html = fromstring(linked(self.brain, self.brain.Title))

        self.assertEqual(1, len(html.xpath('a/img')))

    @skipIf(IS_PLONE_5, 'Plone 5 no longer uses "icon_exp"')
    def test_img_src_to_obj_icon(self):
        self.folder.getTypeInfo().icon_expr_object = Expression(
            'string:folder.jpg')
        self.folder.reindexObject()
        self.brain = getToolByName(self.portal, 'portal_catalog')(
            portal_type="Folder")[0]

        html = fromstring(linked(self.brain, self.brain.Title))

        element = html.xpath('a/img')[0]

        self.assertEqual(
            '%s/folder.jpg' % self.portal.absolute_url(),
            element.attrib.get('src'))

    @skipIf(IS_PLONE_5, 'Plone 5 no longer uses "icon_exp"')
    def test_link_text_is_obj_title(self):
        html = fromstring(linked(self.folder, self.folder.Title()))

        element = html.find('a')

        self.assertEqual(
            self.folder.Title(),
            element.text_content())


class TestLinkedWithoutIcon(TestCase):

    layer = FTWTABLE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        login(self.portal, TEST_USER_NAME)

        self.folder = create(Builder('folder').titled(
            u'the <"escaped"> Title').having(
            description=u'a <"f\xc3\xa4ncy"> description',
            ))

        self.brain = getToolByName(self.portal, 'portal_catalog')(
            portal_type="Folder")[0]

    def test_has_link_if_called_with_a_brain(self):
        html = fromstring(linked_without_icon(self.brain, self.brain.Title))

        self.assertEqual('a', html.find('a').tag)

    def test_has_link_with_obj(self):
        html = fromstring(
            linked_without_icon(self.folder, self.folder.Title()))

        self.assertEqual('a', html.find('a').tag)

    def test_has_no_img_tag(self):
        html = fromstring(
            linked_without_icon(self.folder, self.folder.Title()))

        self.assertEqual([], html.xpath('a/img'))

    def test_link_text_is_obj_title(self):
        html = fromstring(
            linked_without_icon(self.folder, self.folder.Title()))

        element = html.find('a')

        self.assertEqual(
            self.folder.Title(),
            element.text_content())
