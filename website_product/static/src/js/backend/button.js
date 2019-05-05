odoo.define('website_product.backend.button', function (require) {
'use strict';

var WidgetWebsiteButton = require('website.backend.button');
var field_registry = require('web.field_registry');

var WidgetWebsiteProductButton = WidgetWebsiteButton.extend({
    template: 'WidgetWebsiteProductButton',
    });

field_registry.add('website_product_button', WidgetWebsiteProductButton);
});
