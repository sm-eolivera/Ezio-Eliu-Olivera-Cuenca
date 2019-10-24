# -*- coding: utf-8 -*-
from odoo import fields, models


class Partner(models.Model):
    _name = 'library.partner'
    _description = 'Partner'

    x_name = fields.Many2one('res.users', string='Name')
    x_email = fields.Char(string='Email')
    x_address = fields.Text(string='Address')
    x_partner_type = fields.Selection([('customer', 'Customer'), ('author', 'Author')], default="customer", string='Partner_Type')

    x_rental_ids = fields.One2many('library.rental', 'x_customer_id', string='Rentals')
    
