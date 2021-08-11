from flask import Flask
from flask_restful import Api, Resource, reqparse
from urllib import request
import cv2 as cv
import numpy as np
import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir+'\\machine_learning')
# sys.path.append(parentdir+'\\machine_learning\\preprocessing')
from main import main

app = Flask(__name__)
api = Api(app)

process_get_args =  reqparse.RequestParser()
process_get_args.add_argument('img_url',type=str,help="Image URL is required", required=True)



class process(Resource):
    def get(self):
        img_dir = parentdir+'\\machine_learning\\preprocessing\\Photos\\temp.jpg'
        args = process_get_args.parse_args()
        request.urlretrieve(args['img_url'], img_dir)
        grid = main(img_dir)
        return {"Array" : grid}

api.add_resource(process, '/process')

if __name__ == '__main__':
    app.run(debug=True)