# -*- coding: utf-8 -*-
from odoo import models, fields


class Price(models.Model):
    _name = 'library.price'
    _description = 'Price'

    x_name = fields.Char()
    x_duration = fields.Float('Duration in days')
    x_price = fields.Float()
    x_type = fields.Selection([('time', 'Based on time'), ('one', 'Oneshot')], default="time")
