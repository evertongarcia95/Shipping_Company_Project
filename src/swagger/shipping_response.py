from flask_restplus import fields
from src.server.instance import server


api = server.api

post_shipping_status_code_200 = api.model('PostShippingStatusCode200', {
    'Name': fields.String(example='Entrega Ninja', description='Mode of delivery that can be delivered.'),
    'shipping': fields.String(example='R$25.50', description='The freight will be the amount that will be charged for that delivery in question.'),
    'deadline': fields.Integer(example=6, description='To estimated for each delivery.')
})

post_shipping_status_code_400 = api.model('PostShippingStatusCode400', {
    "message": fields.String(example='This field needs to be specified.')
})

post_shipping_status_code_404 = api.model('PostShippingStatusCode404', {
    "message": fields.String(example='There is no delivery method for this product.')
})
