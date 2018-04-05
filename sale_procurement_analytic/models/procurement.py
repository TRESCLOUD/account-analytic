# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, registry, _


class ProcurementOrder(models.Model):
    _inherit = "procurement.order"

    def _get_stock_move_values(self):
        ''' 
        seteamos al move la cuenta analitica que viene desde la orden de venta.
        :return: dictionary
        '''
        res = super(ProcurementOrder, self)._get_stock_move_values()
        if self._fields.get('account_analytic_id', False):
            if self.account_analytic_id:
                #TODO: en los moves el campo se denominado analytic_account_id.
                res.update({'analytic_account_id' : self.account_analytic_id.id})
        return res