# Copyright 2018 Eficent Business and IT Consulting Services S.L.
#   (http://www.eficent.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from mock import patch
from odoo.tests.common import SavepointCase
from ..controllers.main import WebsiteProductPage


class TestController(SavepointCase):

    @classmethod
    def setUpClass(cls):
        super(TestController, cls).setUpClass()
        cls.env = cls.env(context=dict(cls.env.context, tracking_disable=True))
        cls.uom_unit = cls.env.ref('product.product_uom_unit')

        cls.product_sale_ok = cls.env['product.template'].create({
            'name': 'Product sale ok',
            'uom_id': cls.uom_unit.id,
            'uom_po_id': cls.uom_unit.id,
            'sale_ok': True,
        })

        cls.product_no_sale = cls.env['product.template'].create({
            'name': 'Product no sale',
            'uom_id': cls.uom_unit.id,
            'uom_po_id': cls.uom_unit.id,
            'sale_ok': False,
        })

    def test_compute_website_url(self):
        """Test website_url from product.templates."""
        self.assertTrue('/product/' in self.product_no_sale.website_url)

    @patch('odoo.addons.website_product.'
           'controllers.main.request')
    def test_request_product_sale_ok(self, request):
        """Test controller for salable product"""
        # Mock
        request.env = self.env

        ctrl = WebsiteProductPage()
        response = ctrl.products_detail(self.product_sale_ok)
        self.assertTrue('request.render()' in str(response.name))

    @patch('odoo.addons.website_product.'
           'controllers.main.request')
    def test_request_product_no_sale(self, request):
        """Test controller for not salable product"""
        # Mock
        request.env = self.env

        ctrl = WebsiteProductPage()
        response = ctrl.products_detail(self.product_no_sale)
        self.assertTrue('request.render()' in str(response.name))
