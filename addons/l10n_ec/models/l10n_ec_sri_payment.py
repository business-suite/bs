# -*- coding: utf-8 -*-


from odoo import fields, models


class SriPayment(models.Model):

    _name = "l10n_ec.sri.payment"
    _description = "SRI Payment Method"

    name = fields.Char("Name")
    code = fields.Char("Code")
