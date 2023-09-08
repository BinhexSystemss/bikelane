# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright 2019 EquickERP
#
##############################################################################

{
    'name': "Invoice Tax Summary",
    'category': 'Accounting',
    'version': '15.0.1.0',
    'author': 'Equick ERP',
    'description': """
        This Module allows you to show Taxes summary in invoices.
        * Allows you to show taxes summary in customer invoice, credit note, vendor bill and refund.
        * Allows you to show taxes summary in invoice report.
        * No need any configurations.
    """,
    'summary': """Taxes summary in invoice | invoice tax summary | accounting tax summary| taxes on invoice | tax summary in invoice | tax summary in vendor bill | invoice taxes summary | taxes summary in invoice | taxes summary in vendor bill""",
    'depends': ['base', 'account'],
    'price': 10,
    'currency': 'EUR',
    'license': 'OPL-1',
    'website': "",
    'data': [
            'security/ir.model.access.csv',
            'views/account_move_view.xml',
            'views/report_invoice.xml',
    ],
    'images': ['static/description/main_screenshot.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
