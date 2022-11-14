from email.mime import application
from operator import imod
from flask import Flask
from flask_cors.extension import CORS
from flask_restful import Api, Resource
from api.rotatepdf import Rotate_PDF
application = Flask(__name__)
CORS(application)

api = Api(application)

api.add_resource(Rotate_PDF,'/rotate_pdf/')

if __name__ == "__main__":
    application.run(host='0.0.0.0' , port=8080, debug='DEBUG')
    print('Admin is running sucessfully at port')

