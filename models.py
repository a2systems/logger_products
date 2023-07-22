from odoo import tools, models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import date,datetime


class ProductTemplate(models.Model):
    _inherit = "product.template"

    def write(self, vals):
        if 'standard_price' in vals:
            logging_values = {
                'product_tmpl_id': self.id,
                'field_name': 'standard_price',
                'old_val': self.standard_price,
                'new_val': vals.get('standard_price')
                }
            logging_id = self.env['product.logging'].create(logging_values)
        return super(ProductTemplate, self).write(vals)

    logging_ids = fields.One2many(
            comodel_name='product.logging',
            inverse_name='product_tmpl_id',
            string='Logging')

class ProductLogging(models.Model):
    _name = 'product.logging'
    _description = 'product.logging'

    product_tmpl_id = fields.Many2one('product.template','Producto')
    field_name = fields.Char('Campo')
    old_val = fields.Float('Viejo valor')
    new_val = fields.Float('Nuevo valor')
