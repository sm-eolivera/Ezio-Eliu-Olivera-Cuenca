# -*- coding: utf-8 -*-
from odoo import fields, models, api


class Books(models.Model):
    _name = 'library.book'
    _description = 'Book'
    
    
    name = fields.Char(string='Title')
    lauthor =fields.Char(computer ='_compute_lauthor', store=True)
    author_ids = fields.Many2many("library.partner", string="Authors")
    edition_date = fields.Date()
    isbn = fields.Char(string='ISBN')
    publisher_id = fields.Many2one('library.publisher', string='Publisher')
    

#   copy_ids = fields.One2many('library.copy', 'book_id', string="Book Copies")
    rental_ids = fields.One2many('library.rental', 'book_id', string='Rentals')
    is_book = fields.Boolean(string='Is a Book', default=False)   
    
#     @api.one
#     @api.depends('lauthor')
#     def _compute_lauthor(self):
#         if self.edition_date:
#             self.lauthor = fields.Date().today
#         else: 
#             return
        
    @api.onchange(name)
    def _onchange(self):
        if self.name:
            self.is_book = True
        else:
            return
        
# class BookCopy(models.Model):
#     _name = 'library.copy'
#     _description = 'Book Copy'
#     _rec_name = 'reference'

#     book_id = fields.Many2one('product.product', string="Book", domain=[('is_book', "=", True)], required=True, ondelete="cascade", delegate=True)
#     reference = fields.Char(required=True, string="Ref")

# #     rental_ids = fields.One2many('library.rental', 'copy_id', string='Rentals')
#     book_state = fields.Selection([('available', 'Available'), ('rented', 'Rented'), ('lost', 'Lost')], default="available")
    
#     state = fields.Selection([
#             ('concept', 'Concept'),
#             ('started', 'Started'),
#             ('progress', 'In progress'),
#             ('finished', 'Done')
#             ],default='concept')
      
#     @api.one
#     def available_progressbar(self):
#         self.write({
#         'book_state': 'available',
#     })

#     @api.one
#     def rented_progressbar(self):
#         self.write({
#         'book_state': 'rented'
#     })

#     @api.one
#     def lost_progressbar(self):
#         self.write({
#         'book_state': 'lost'
#     })

