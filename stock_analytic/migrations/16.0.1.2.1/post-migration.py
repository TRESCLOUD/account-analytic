# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openupgradelib import openupgrade

@openupgrade.migrate(use_env=True)
def migrate(env, version):
    """
    A todos los registros en la tabla account_analytic_line que tengan un valor negativo en el campo unit_amount
    lo convierte a positivo mediante SQL para no desencadenar algún método
    """
    env.cr.execute("""
        UPDATE account_analytic_line
        SET unit_amount = ABS(unit_amount)
        WHERE unit_amount < 0
    """)