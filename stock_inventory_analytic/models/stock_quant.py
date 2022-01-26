# -*- coding: utf-8 -*-
from odoo import fields, models, api


class StockQuant(models.Model):
    _inherit = "stock.quant"

    def _get_inventory_move_values(self, qty, location_id, location_dest_id, out=False):
        """ Called when user manually set a new quantity (via `inventory_quantity`)
            just before creating the corresponding stock move.
        """
        res = super(StockQuant, self)._get_inventory_move_values(qty, location_id, location_dest_id, out=out)
        if self.analytic_account_id:
            res["analytic_account_id"] = self.analytic_account_id.id
        return res

    @api.model
    def _get_inventory_fields_write(self):
        '''
        Add analytic_account_id to allowed fields create
        '''
        fields = super(StockQuant, self)._get_inventory_fields_write()
        fields += ['analytic_account_id']
        return fields

    analytic_account_id = fields.Many2one(
        comodel_name="account.analytic.account",
        string="Analytic Account",
        default=lambda self: self.env.user.company_id.analytic_account_id.id,
    )
