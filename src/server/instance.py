from flask import Flask, Blueprint
from flask_restplus import Api


URL_PREFIX = '/shipping'

class Server(object):
    def __init__(self):
        self.app = Flask(__name__)
        self.blueprint = Blueprint('api', __name__, url_prefix=URL_PREFIX)
        self.api = Api(
            doc='/docs',
            title="Transport Delivery Project",
            description="API for calculation and selection of shipping modalities",
            version='0.0.1',
            contact='',
            default='',
            default_label='KaBuM')

        self.shipping = self.shipping()

    def shipping(self, ):
        return self.api.namespace(
            name='Shipping Company',
            description='.',
            path='/'
        )

    def run(self,):
        self.app.run(
            
            debug=True
            
        )