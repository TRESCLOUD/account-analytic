# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'    

    def _prepare_analytic_distribution_line(self, distribution, account_id, distribution_on_each_plan):
        # FIX TRESCLOUD: Arreglo en la creación de apuntes analíticos para que la cantidad sea positiva
        # Los apuntes analíticos siempre deben ser positivas y en el caso de que se creen a partir de un movimiento de salida o de desecho, la cantidad debe ser positiva
        vals = super()._prepare_analytic_distribution_line(distribution, account_id, distribution_on_each_plan)

        if self.quantity < 0:
            vals.update({'unit_amount': abs(self.quantity)})
        return vals
