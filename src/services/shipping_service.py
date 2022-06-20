from src.exceptions.exceptions_errors import NotFound, Validation
import requests


class ShippingService():
    def shipping_ninja(self, height: int, width: int, weight: int) -> dict:
        specification = 10 <= height <= 200 and 6 <= width <= 140 and weight > 0
        if specification:
            shipping = (weight * 0.3 ) / 10
            ninja_delivery = {'Name': 'Entrega Ninja',
                  'cost_of_freight': f'R${shipping:.2f}', 'deadline': 6}
            return ninja_delivery
        else:
            None

    def shipping_kabum(self, height: int, width: int, weight: int) -> dict:
        especification = 5 <= height <= 140 and 13 <= width <= 125 and weight > 0
        if especification:
            shipping = (weight * 0.2 ) / 10
            kabum_delivery = {'Name': 'Entrega KaBuM',
                  'cost_of_freight': f'R${shipping:.2f}', 'deadline': 4}
            return kabum_delivery
        else:
            None

    def shipping_validations_fields(self, height: int, width: int, weight: int) -> None:
        if not height:
            raise Validation("The height field must be specified.")

        elif not width:
            raise Validation("The width field must be specified.")

        elif not weight:
            raise Validation("The weight field must be specified.")

    def post_shipping_validation(self, request_body) -> dict:
        height = request_body["height"]
        width = request_body["width"]
        weight = request_body["weight"]

        
        self.shipping_validations_fields(height, width, weight)
    
        ninja = self.shipping_ninja(height, width, weight)
        kabum = self.shipping_kabum(height, width, weight)

        if ninja == None and kabum == None:
            raise NotFound("There is no delivery method for this product.")
        elif ninja == None:
            return [kabum]
        elif kabum == None:
            return [ninja]
        else:
            return [ninja, kabum]
