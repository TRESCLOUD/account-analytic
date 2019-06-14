# -*- coding: utf-8 -*-
# © 2016 Antonio Espinosa - <antonio.espinosa@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class AccountAssetAsset(models.Model):
    _inherit = "account.asset.asset"
    # CODIGO MODIFICADO POR TRESCLOUD
    analytic_account_id = fields.Many2one(
        string="Analytic account",
        comodel_name='account.analytic.account',
        readonly=True,
        states={'draft': [('readonly', False)]},
        track_visibility='onchange'
    )
    # FIN DEL CODIGO MODIFICADO POR TRESCLOUD
