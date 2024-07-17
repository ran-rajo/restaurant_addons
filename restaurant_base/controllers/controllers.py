# -*- coding: utf-8 -*-
# from odoo import http


# class RestaurantBase(http.Controller):
#     @http.route('/restaurant_base/restaurant_base', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/restaurant_base/restaurant_base/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('restaurant_base.listing', {
#             'root': '/restaurant_base/restaurant_base',
#             'objects': http.request.env['restaurant_base.restaurant_base'].search([]),
#         })

#     @http.route('/restaurant_base/restaurant_base/objects/<model("restaurant_base.restaurant_base"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('restaurant_base.object', {
#             'object': obj
#         })
