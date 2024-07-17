# -*- coding: utf-8 -*-
# from odoo import http


# class RestaurantPos(http.Controller):
#     @http.route('/restaurant_pos/restaurant_pos', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/restaurant_pos/restaurant_pos/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('restaurant_pos.listing', {
#             'root': '/restaurant_pos/restaurant_pos',
#             'objects': http.request.env['restaurant_pos.restaurant_pos'].search([]),
#         })

#     @http.route('/restaurant_pos/restaurant_pos/objects/<model("restaurant_pos.restaurant_pos"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('restaurant_pos.object', {
#             'object': obj
#         })
