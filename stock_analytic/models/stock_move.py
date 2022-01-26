# -*- coding: utf-8 -*-
from odoo import api, fields, models


class StockMove(models.Model):
    _inherit = 'stock.move'

    def _prepare_account_move_line(self, qty, cost, credit_account_id, debit_account_id, description):
        '''
        Add the analytical account and analytical labels to the invoice line
        '''
        self.ensure_one()
        res = super(StockMove, self)._prepare_account_move_line(qty, cost, credit_account_id, debit_account_id, description)
        for line in res:
            if line[2]["account_id"] != self.product_id.categ_id.property_stock_valuation_account_id.id:
                if self.analytic_account_id:
                    line[2].update({"analytic_account_id": self.analytic_account_id.id})
                if self.analytic_tag_ids:
                    line[2].update({"analytic_tag_ids": [(6, 0, self.analytic_tag_ids.ids)]})
        return res

    @api.model
    def _prepare_merge_moves_distinct_fields(self):
        '''
                Prepare the fields to allow you to create the moves
        '''
        fields = super()._prepare_merge_moves_distinct_fields()
        fields.append("analytic_account_id")
        return fields

    analytic_account_id = fields.Many2one(
        string='Analytic Account',
        comodel_name='account.analytic.account',
    )
    analytic_tag_ids = fields.Many2many(
        'account.analytic.tag',
        string='Analytic Tags'
    )


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    analytic_account_id = fields.Many2one(
        related='move_id.analytic_account_id'
    )
