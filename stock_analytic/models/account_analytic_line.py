# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    # CRUD METHODS
    @api.model_create_multi
    def create(self, vals):
        """
        Antes de crear, se verifica que el campo de cantidad sea positivo
        Si no lo es, se lo convierte a positivo
        """
        for val in vals:
            if 'unit_amount' in val:
                if val['unit_amount'] < 0:
                    val['unit_amount'] = abs(val['unit_amount'])
        return super().create(vals)