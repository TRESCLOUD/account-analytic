# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    analytic_account_id = fields.Many2one(
        related="company_id.analytic_account_id",
        readonly=False
    )
    analytic_tag_ids = fields.Many2many(
        related="company_id.analytic_tag_ids",
        readonly=False
    )
