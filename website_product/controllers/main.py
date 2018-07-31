# Copyright 2018 Eficent Business and IT Consulting Services S.L.
#   (http://www.eficent.com)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import http
from odoo.http import request


class WebsiteProductPage(http.Controller):

    # Do not use semantic controller due to SUPERUSER_ID
    @http.route(['/product/<model("product.template"):product>'], type='http',
                auth="public", website=True)
    def products_detail(self, product, **post):
        if isinstance(product, request.env['product.template'].__class__):
            is_website_publisher = request.env['res.users'].has_group(
                'website.group_website_publisher')
            if product.website_published or is_website_publisher:
                values = {
                    'main_object': product,
                    'product': product,
                    'edit_page': False
                }
                return request.render("website_product.product_page", values)
        return request.not_found()
