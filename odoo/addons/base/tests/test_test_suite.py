# -*- coding: utf-8 -*-


from unittest import TestCase

from odoo.tests import MetaCase


class TestTestSuite(TestCase, metaclass=MetaCase):

    def test_test_suite(self):
        """ Check that OdooSuite handles unittest.TestCase correctly. """
