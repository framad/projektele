# -*- coding: utf-8 -*-

from odoo import models, fields # Mandatory
import datetime


class RekapSo(models.Model):
    _name = 'projektele.rekap_so' # name_of_module.name_of_class 
    _description = 'Projek Tele Rekap SO' # Some note of table

    # Header
    product = fields.Char()
    product_name = fields.Char()
    id_produk = fields.Many2one('product.template')
    total_product = fields.Float()
    quantity = fields.Float()
    transaction_date = fields.Datetime()
    rekap_so_id = fields.Many2one(comodel_name="sale.order")
    total_rekap_id = fields.Many2one(comodel_name="sale.order")