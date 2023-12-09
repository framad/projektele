# -*- coding: utf-8 -*-

from odoo import models, fields, api # Mandatory
import datetime
from odoo.exceptions import ValidationError

class Material(models.Model):
    _name = 'projektele.material' # name_of_module.name_of_class 
    _description = 'Material' # Some note of table

    # Header
    material_code = fields.Char()
    material_name = fields.Char()
    material_type = fields.Selection([
        ('Fabric', 'Fabric'),
        ('Jeans', 'Jeans'),
        ('Cotton', 'Cotton')
    ])
    material_buy_price = fields.Integer()
    related_supplier = fields.Many2one('projektele.supplier')

    # @api.model
    # def create(self, values):
    #     print(self.material_buy_price, "ini material harga")
    #     if  self.material_buy_price < 100:
    #         raise ValidationError(
    #             "Material Buy Price tidak boleh kurang dari 100")
    #     res = super(Material, self).create(values)
    #     return res
    
    @api.constrains('material_buy_price')
    def check_name(self):
        """ make sure name 10-15 alphabets and spaces"""
        for rec in self:
            if self.material_buy_price < 100:
                raise ValidationError(
                    "Material Buy Price tidak boleh kurang dari 100")