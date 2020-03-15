from flask_restful import Resource, reqparse
import flask
import requests
import application.config as config
import json
from application.db import Session, Person

class PersonList(Resource):
    def post(self, id):
        """  """
        try:
            data = ""
            return flask.make_response(flask.jsonify({'data': data}), 201)
        except Exception as e:
            print("error: -", e)
            return flask.make_response(flask.jsonify({'error': str(e)}), 400)

    def get(self, id):
        """  """
        try:
            session = Session()
            person = Person(fname="hi")
            session.add(person)
            session.commit()

            data = list(session.query(Person).all())
            arr = []
            for x in data:
                arr.append(json.loads(x))

            print(arr)
            return flask.make_response(flask.jsonify({'data': arr}), 200)
        except Exception as e:
            print("error: -", e)
            return flask.make_response(flask.jsonify({'error': str(e)}), 400)

    def put(self, id):
        """  """
        try:
            data = ""
            return flask.make_response(flask.jsonify({'data': data}), 200)
        except Exception as e:
            print("error: -", e)
            return flask.make_response(flask.jsonify({'error': str(e)}), 400)

    def delete(self, id):
        """  """
        try:
            data = ""
            return flask.make_response(flask.jsonify({'data': data}), 204)
        except Exception as e:
            print("error: -", e)
            return flask.make_response(flask.jsonify({'error': str(e)}), 400)

