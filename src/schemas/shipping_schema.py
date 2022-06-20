
from marshmallow import fields, Schema

    
class ShippingSchema(Schema):
    height = fields.Integer(required=True, description='Measurement parameter for delivery.', error="This field needs to be specified.")
    width = fields.Integer(required=True, description='Measurement parameter for delivery.', error="This field needs to be specified.")
    weight = fields.Integer(required=True, description='Weight parameter for delivery.', error="This field needs to be specified.")