# -*- coding: utf-8 -*-

import base64

from odoo import fields, api, models


class POSOrder(models.Model):
    _inherit = 'pos.order'

    def _prepare_invoice_vals(self):
        vals = super()._prepare_invoice_vals()
        if self.company_id.country_id.code == 'SA':
            vals.update({'l10n_sa_confirmation_datetime': self.date_order})
        return vals
