from flask_restplus import Resource
from flask_accepts import accepts
from flask import request
from src.schemas.shipping_schema import ShippingSchema
from src.services.shipping_service import ShippingService
from src.exceptions.exceptions_errors import NotFound, Validation
from src.server.instance import server
from src.swagger import shipping_response, status_code_descriptions


shipping = server.shipping

@shipping.route('/shipping', methods=['POST'])
class ShippingController(Resource):
    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.shipping_service = ShippingService()

    @shipping.response(200, status_code_descriptions.code_200, shipping_response.post_shipping_status_code_200)
    @shipping.response(400, status_code_descriptions.code_400, shipping_response.post_shipping_status_code_400)
    @shipping.response(404, status_code_descriptions.code_404, shipping_response.post_shipping_status_code_404)
    @accepts(schema=ShippingSchema, api=shipping)
    def post(self):
        try:
            request_body = request.json
            return self.shipping_service.post_shipping_validation(request_body)

        except Validation as ex:
            return {"message": ex.message}, ex.status

        except NotFound as ex:
            return {"message": ex.message}, ex.status
