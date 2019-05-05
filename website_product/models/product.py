# Copyright 2018 Eficent Business and IT Consulting Services S.L.
#   (http://www.eficent.com)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import api, fields, models
from odoo.addons.http_routing.models.ir_http import slug
from odoo.tools.translate import html_translate


class ProductTemplate(models.Model):
    _name = 'product.template'
    _inherit = ['product.template',
                'website.seo.metadata',
                'website.product.published.mixin']


class ProductProduct(models.Model):
    _inherit = 'product.product'
    _inherits = {'product.template': 'product_tmpl_id'}
