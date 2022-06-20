from email.mime import application
from flask import Flask, Blueprint
from flask_restplus import Api


class Server():
    def __init__(self, ) -> None:
        self.app = Flask(__name__)
        self.blueprint = Blueprint('api', __name__, url_prefix='/api')
        self.api = Api(
            doc='/docs',
            info='Internal system for shipping products by carriers.',
            title='Transport Delivery Project Documentation.',
            version='1.0',
            description='API for calculation and selection of shipping modalities.'
        )
        self.api.init_app(self.blueprint)
        self.shipping = self.shipping()
        self.app.register_blueprint(self.blueprint)

    def shipping(self, ):
        return self.api.namespace(
            name='Shipping Company',
            description='.',
            path='/'
        )

    def run(self,):
        self.app.run(
            port=5000,
            debug=True,
            host='0.0.0.0'
        )

server = Server()

application = server.app
