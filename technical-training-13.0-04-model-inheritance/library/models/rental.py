# -*- coding: utf-8 -*-
from odoo import fields, models


class Rentals(models.Model):
    _name = 'library.rental'
    _description = 'Book rental'

    x_customer_id = fields.Many2one('library.partner', string='Customer')
    x_book_id = fields.Many2one('library.book', string='Book')

    x_rental_date = fields.Date(string='Rental_Date')
    x_return_date = fields.Date(string='Return_Date')

    x_customer_address = fields.Text(related='x_customer_id.x_address', string='Address')
    x_customer_email = fields.Char(related='x_customer_id.x_email', string='Email')

    x_book_authors = fields.Many2many(related='x_book_id.x_author_ids', string='Author')
    x_book_edition_date = fields.Date(related='x_book_id.x_edition_date', string='Edition_Date')
    x_book_publisher = fields.Many2one(related='x_book_id.x_publisher_id', string='Publisher')
