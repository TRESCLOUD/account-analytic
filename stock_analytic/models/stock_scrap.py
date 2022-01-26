# -*- coding: utf-8 -*-
from odoo import api, fields, models


class StockScrap(models.Model):
    _inherit = 'stock.scrap'

    def _prepare_move_values(self):
        '''
        Add the analytical account and analytical labels to the invoice line
        '''
        res = super()._prepare_move_values()
        res.update(
            {
                "analytic_account_id": self.analytic_account_id.id,
                "analytic_tag_ids": [(6, 0, self.analytic_tag_ids.ids)],
            }
        )
        return res

    analytic_account_id = fields.Many2one(
        string="Analytic Account",
        comodel_name="account.analytic.account"
    )
    analytic_tag_ids = fields.Many2many(
        "account.analytic.tag",
        string="Analytic Tags"
    )
