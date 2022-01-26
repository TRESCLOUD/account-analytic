# -*- coding: utf-8 -*-
from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    analytic_account_id = fields.Many2one(
        "account.analytic.account",
        string="Default Analytic Account on Inventory Adjustment Line",
    )
    analytic_tag_ids = fields.Many2many(
        "account.analytic.tag",
        string="Default Analytic Tags on Inventory Adjustment Line",
    )
