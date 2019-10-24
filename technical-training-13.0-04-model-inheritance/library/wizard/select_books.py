# -*- coding: utf-8 -*-
from odoo import api, exceptions, fields, models


class SelectBooksToRent(models.TransientModel):
    _name = 'library.wizard'
    _description = 'Wizard to select books to rent'

    @api.model
    def default_get(self, fields):
        res = super(SelectBooksToRent, self).default_get(fields)
        res.update({'x_copy_ids': [(6, 0, self._context.get('active_ids', []))]})
        return res

    x_copy_ids = fields.Many2many('library.copy', string="Book copies", required=True)
    x_customer_id = fields.Many2one('res.partner', string="Customer")
    x_rental_ids = fields.Many2many('library.rental')
    x_return_date = fields.Date()

    @api.model
    def create(self, vals):
        res = super(SelectBooksToRent, self).create(vals)
        return res

    