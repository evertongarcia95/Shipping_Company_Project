from flask_restplus import Resource
from flask import request
from src.services.shipping_service import ShippingService
from src.server.instance import server


shipping = server.shipping

@shipping.route('/', methods=['POST'])
class ShippingController(Resource):
    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.shipping_service = ShippingService()
  
    def post(self):
        try:
            request_body = request.json
            return self.shipping_service.post_shipping(request_body)
        
        # except Validatio as ex:
        #     return {"message": ex.message}, ex.status

        except Exception as ex:
            #logger(request, str(ex), 'post shipping', request_body)
            return {"message": "Error "}, 500
