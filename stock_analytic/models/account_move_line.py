# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'    

    def _prepare_analytic_distribution_line(self, distribution, account_id, distribution_on_each_plan):
        # Los apuntes analíticos siempre deben ser positivas y más aún casos en que se creen a partir de un movimiento de salida o de desecho, donde su cantidad es negativa
        vals = super()._prepare_analytic_distribution_line(distribution, account_id, distribution_on_each_plan)

        if self.quantity < 0:
            vals.update({'unit_amount': abs(self.quantity)})
        return vals
