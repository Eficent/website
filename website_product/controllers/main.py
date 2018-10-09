# Copyright 2018 Eficent Business and IT Consulting Services S.L.
#   (http://www.eficent.com)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import http
from odoo.http import request


class WebsiteProductPage(http.Controller):

    @http.route(['/product/<model("product.template"):product>'], type='http',
                auth="public", website=True)
    def products_detail(self, product, **post):
        if product.exists:
            if product.website_published or self.is_website_publisher:
                values = {
                    'main_object': product,
                    'product': product,
                    'edit_page': False
                }
                return request.render("website_product.product_page", values)
        return request.not_found()

    @staticmethod
    def _is_website_publisher():
        return request.env['res.users'].has_group(
            'website.group_website_publisher')
