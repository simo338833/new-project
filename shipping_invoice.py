from odoo import models, fields, api

class ShippingInvoice(models.Model):
    _name = 'shipping.invoice'
    _description = 'Shipping Supplier Invoice'

    supplier_name = fields.Char('Supplier Name')
    invoice_number = fields.Char('Invoice Number')
    amount_due = fields.Float('Amount Due')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('paid', 'Paid')
    ], string='State', default='draft')

    def action_confirm(self):
        for record in self:
            # تغيير حالة الفاتورة إلى "مؤكد"
            record.state = 'confirmed'
        return True
