# Copyright 2021 Trescloud - Adrian Lima
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
{
    "name": "Stock Analytic",
    "version": "15.0",
    "category": "Warehouse Management",
    "license": "AGPL-3",
    "author": "Trescloud, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/account-analytic",
    "depends": [
        "stock_account",
        "analytic"
    ],
    "data": [
        'views/stock_move_views.xml',
        'views/stock_scrap.xml'
    ],
}
