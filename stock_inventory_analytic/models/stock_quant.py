# -*- coding: utf-8 -*-
from odoo import fields, models


class StockQuant(models.Model):
    _inherit = "stock.quant"

    def _get_inventory_move_values(self, qty, location_id, location_dest_id, out=False):
        """ Called when user manually set a new quantity (via `inventory_quantity`)
            just before creating the corresponding stock move.
        """
        res = super(StockQuant, self)._get_inventory_move_values(qty, location_id, location_dest_id, out=out)
        if self.analytic_account_id:
            res["analytic_account_id"] = self.analytic_account_id.id
        # if self.analytic_tag_ids:
        #     res["analytic_tag_ids"] = [(6, 0, self.analytic_tag_ids.ids)]
        return res

    analytic_account_id = fields.Many2one(
        comodel_name="account.analytic.account",
        string="Analytic Account",
        default=lambda self: self.env.user.company_id.analytic_account_id.id,
    )
    # analytic_tag_ids = fields.Many2many(
    #     comodel_name="account.analytic.tag",
    #     groups='base.group_system',
    #     string="Analytic Tags",
    #     default=lambda self: self.env.user.company_id.analytic_tag_ids.ids,
    # )
