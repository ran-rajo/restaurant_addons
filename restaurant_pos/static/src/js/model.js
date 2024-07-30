odoo.define('pos_restaurant.floors', function (require) {
    "use strict";

    var models = require('point_of_sale.models');
    models.PosModel = models.PosModel.extend({
        initialize:function(attributes){
            this.is_to_invoice();
        }
        
    });
});