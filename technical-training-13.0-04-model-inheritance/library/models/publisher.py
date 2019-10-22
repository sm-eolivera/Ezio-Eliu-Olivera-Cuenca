# -*- coding: utf-8 -*-
from odoo import fields, models


class Editor(models.Model):
    _name = 'library.publisher'
    _description = 'Publisher'

    x_name = fields.Char(string='Name')
