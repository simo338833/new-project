# -*- coding: utf-8 -*-
{
    'name': 'Shipping Invoice Management',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Manage shipping invoices for export purposes',
    'depends': ['base', 'account', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/shipment_views.xml',
        'views/invoice_views.xml',
    ],
    'installable': True,
    'application': True,
}

