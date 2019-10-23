# -*- coding: utf-8 -*-
from odoo import fields, models, api

from odoo.exceptions import ValidationError


class Books(models.Model):
    _name = 'library.book'
    _description = 'Book'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    x_name = fields.Char(string='Title')
    x_lauthor = fields.Char(compute ='_compute_lauthor',string='Author', store=True)
    x_author_ids = fields.Many2many("library.partner", string="Authors")
    x_edition_date = fields.Date(string='Edition_Date')
    x_isbn = fields.Char(string='ISBN')
    x_publisher_id = fields.Many2one('library.publisher', string='Publisher')
    

    x_copy_ids = fields.One2many('library.copy', 'x_book_id', string="Book Copies")
    x_rental_ids = fields.One2many('library.rental', 'x_book_id', string='Rentals')
    x_is_book = fields.Boolean(string='Is a Book', default=True)

    x_book_state = fields.Selection([('concept', 'Concept'),('started', 'Started'),('progress', 'In progress'),('finished', 'Done')],default='concept',string='Book_State')
      
#     @api.one
#     def concept_progressbar(self):
#         self.write({
#         'x_book_state': 'concept',
#     })

    
#    @api.onchange('x_author_ids')
#     def _compute_lauthor(self):
#         raise ValidationError("Asd")
#         if self.x_author_ids:
#             self.x_lauthor = self.x_author_ids.x_name
#         else: 
#             return
    @api.depends('x_author_ids')
    def _compute_lauthor(self):
        for record in self:
            if record.x_author_ids:
                record.x_lauthor = record.x_author_ids.x_name 
            else: 
                return
    
        
    @api.onchange('x_name')
    def _onchange(self):
        if self.x_name:
            self.x_edition_date = fields.Date().today()
        else:
            return

        
class BookCopy(models.Model):
    _name = 'library.copy'
    _description = 'Book Copy'
    _rec_name = 'x_reference'

    x_book_id = fields.Many2one('library.book', string="Book", domain=[('x_is_book', "=", True)], required=True, ondelete="cascade", delegate=True)
    x_reference = fields.Char(required=True, string="Ref")

    x_rental_ids = fields.One2many('library.rental', 'x_copy_id', string='Rentals')
    x_book_state = fields.Selection([('available', 'Available'), ('rented', 'Rented'), ('lost', 'Lost')], default="available")
    
