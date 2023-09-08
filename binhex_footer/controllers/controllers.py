# -*- coding: utf-8 -*-
# from odoo import http


# class BinhexFooter(http.Controller):
#     @http.route('/binhex_footer/binhex_footer/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/binhex_footer/binhex_footer/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('binhex_footer.listing', {
#             'root': '/binhex_footer/binhex_footer',
#             'objects': http.request.env['binhex_footer.binhex_footer'].search([]),
#         })

#     @http.route('/binhex_footer/binhex_footer/objects/<model("binhex_footer.binhex_footer"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('binhex_footer.object', {
#             'object': obj
#         })
