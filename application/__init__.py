from flask import Flask, request, g, render_template
from flask_restful import Resource, reqparse
from flask_restful_swagger_3 import Api
from flask_cors import CORS
import os
from json import dumps
import application.endpoints as endpoints
import application.config as config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app, version='1', contact={"name":""}, license={"name":"Online Dienst Dokumentation"}, api_spec_url='/api/swagger')


api.add_resource(endpoints.PersonList,'/api/v1/person/<string:id>', '/api/v1/person/')

@app.route("/")
def index():
    """serve the ui"""
    return render_template("index.html")
        