# -*- coding: utf-8 -*-
from odoo import fields, models, api

from odoo.exceptions import ValidationError


class Rentals(models.Model):
    _name = 'library.rental'
    _description = 'Book rental'

    x_customer_id = fields.Many2one('library.partner', string='Customer')
    x_book_id = fields.Many2one('library.book', string='Book')
    x_copy_id = fields.Many2one('library.copy', string="Book Copy", domain=[('x_book_state', '=', 'available')], required=True)
    x_DateVal = fields.Char(compute ='_compute_dateVal',string='Date', store=True)

    x_rental_date = fields.Date(string='Rental_Date')
    x_return_date = fields.Date(string='Return_Date')

    x_customer_address = fields.Text(related='x_customer_id.x_address', string='Address')
    x_customer_email = fields.Char(related='x_customer_id.x_email', string='Email')

    x_book_authors = fields.Many2many(related='x_book_id.x_author_ids', string='Author')
    x_book_edition_date = fields.Date(related='x_book_id.x_edition_date', string='Edition_Date')
    x_book_publisher = fields.Many2one(related='x_book_id.x_publisher_id', string='Publisher')
    
#   Validate when the return date is less than the current date -Painted Field
    @api.depends('x_return_date')
    def _compute_dateVal(self):
        for record in self:
            
            if record.x_return_date < fields.Date().today(): 
                record.x_DateVal = 'Atrasado'
            else: 
                record.x_DateVal = 'A tiempo'

# current date validation
    @api.constrains('x_rental_date')
    def _onchange(self):
        if (self.x_rental_date or self.x_return_date) < fields.Date().today():
            raise ValidationError("Fecha menor a la actual")
        if self.x_rental_date > self.x_return_date:
            raise ValidationError("Error en la fecha de retorno")
        else:
            return
