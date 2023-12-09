# -*- coding: utf-8 -*-

from odoo import models, fields # Mandatory
import datetime


class Supplier(models.Model):
    _name = 'projektele.supplier' # name_of_module.name_of_class 
    _description = 'Material' # Some note of table

    # Header
    name = fields.Char()