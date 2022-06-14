import requests

class ShippingService():
    def __init__(self, height, width, weight):
        self.height = height
        self.width = width
        self.weight = weight

    def post_shipping(self, height, width, weight):
        pass