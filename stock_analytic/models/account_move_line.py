# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'    

    def _prepare_analytic_distribution_line(self, distribution, account_id, distribution_on_each_plan):
        # FIX TRESCLOUD: Arreglo en la creación de apuntes analíticos para que la cantidad sea positiva
        # Los apuntes analíticos siempre deben ser positivas y en el caso de que se creen a partir de un movimiento de salida o de desecho, la cantidad debe ser positiva
        vals = super()._prepare_analytic_distribution_line(distribution, account_id, distribution_on_each_plan)
        company = self.company_id

        # Validamos que el apunte analítico a crear sea de una compañía ecuatoriana
        is_ec_analytic_line = company and company.account_fiscal_country_id.code == 'EC'

        # Validamos que la cuenta analítica a crear sea de los diarios de inventario y que la cantidad sea negativa
        stock_journals = self.env['product.category'].with_company(company).search([('property_stock_journal', '!=', False)]).mapped('property_stock_journal')
        journal = self.journal_id

        if is_ec_analytic_line and \
            journal.id in stock_journals.ids and \
            self.quantity < 0:
            vals.update({'unit_amount': abs(self.quantity)})
        return vals
