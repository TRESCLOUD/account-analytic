# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'    

    def _prepare_analytic_distribution_line(self, distribution, account_id, distribution_on_each_plan):
        # Los apuntes analíticos siempre deben ser positivas y más aún casos en que se creen a partir de un movimiento de salida o de desecho, donde su cantidad es negativa
        vals = super()._prepare_analytic_distribution_line(distribution, account_id, distribution_on_each_plan)

        if self.quantity < 0:
            # Validamos que la cuenta analítica a crear sea de los diarios de inventario para los productos que tienen ajustes de inventario y que la cantidad sea negativa
            stock_journals = self.env['product.category'].with_company(self.company_id).search([('property_stock_journal', '!=', False)]).mapped('property_stock_journal')
            if stock_journals and self.journal_id.id in stock_journals.ids:
                vals.update({'unit_amount': abs(self.quantity)})
        return vals
