from odoo import models, fields, api

class Supplier(models.Model):
    _name = 'shipping.supplier'
    _description = 'Shipping Supplier'

    name = fields.Char(string='Name', required=True)
    supplier_name = fields.Char(string='Supplier Name')  # تم إضافة هذا الحقل
    address = fields.Char(string='Address')
    vat_number = fields.Char(string='VAT Number')
    bank_account = fields.Char(string='Bank Account')
    invoice_number = fields.Char(string='Invoice Number')  # إضافة حقل رقم الفاتورة


class Shipment(models.Model):
    _name = 'shipping.shipment'
    _description = 'Shipping Shipment'

    supplier_id = fields.Many2one('shipping.supplier', string='Supplier')
    shipment_date = fields.Date(string='Shipment Date')
    destination_country = fields.Char(string='Destination Country')
    weight = fields.Float(string='Weight (kg)')
    volume = fields.Float(string='Volume (m3)')
    goods_type = fields.Char(string='Type of Goods')
    client_invoice_number = fields.Char(string='Client Invoice Number')
    shipping_cost = fields.Float(string='Shipping Cost')
    additional_fees = fields.Float(string='Additional Fees')
    expected_arrival = fields.Date(string='Expected Arrival Date')
    tracking_number = fields.Char(string='Tracking Number')
    packaging_type = fields.Char(string='Packaging Type')
    shipment_insurance = fields.Float(string='Insurance Cost')

    # حساب التكلفة الإجمالية مع إضافة الرسوم الإضافية والتأمين
    @api.depends('shipping_cost', 'additional_fees', 'shipment_insurance')
    def _compute_total_cost(self):
        for record in self:
            record.total_cost = record.shipping_cost + record.additional_fees + record.shipment_insurance

    total_cost = fields.Float(string='Total Cost', compute='_compute_total_cost', store=True)


class ShippingInvoice(models.Model):
    _name = 'shipping.invoice'
    _description = 'Shipping Invoice'

    shipment_id = fields.Many2one('shipping.shipment', string='Shipment', required=True)
    invoice_number = fields.Char(string='Invoice Number', required=True)  # إضافة حقل رقم الفاتورة
    supplier_name = fields.Char(string='Supplier Name', related='shipment_id.supplier_id.supplier_name')  # جلب اسم المورد من الشحنة
    invoice_date = fields.Date(string='Invoice Date')
    amount_due = fields.Float(string='Amount Due', related='shipment_id.total_cost')
    payment_status = fields.Selection([('unpaid', 'Unpaid'), ('paid', 'Paid')], string='Payment Status', default='unpaid')
