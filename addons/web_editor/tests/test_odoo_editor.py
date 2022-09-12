# -*- coding: utf-8 -*-


import odoo.tests

@odoo.tests.tagged("post_install", "-at_install")
class TestOdooEditor(odoo.tests.HttpCase):

    def test_odoo_editor_suite(self):
        self.browser_js('/web_editor/static/lib/odoo-editor/test/editor-test.html', "", "", timeout=1800)
