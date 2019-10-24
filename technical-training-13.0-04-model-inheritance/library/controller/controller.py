from odoo import http

class Library(http.Controller):
    @http.route('/library/library/', auth='public')
    def index(self, **kw):
        return "Hello, world"