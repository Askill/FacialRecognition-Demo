from flask_restful import Resource, reqparse
import flask
import requests
import application.config as config
import json
from application.db import Session, Person, Fingerprint

class PersonList(Resource):
    def post(self, id = None):
        """  """
        try:
            data = ""
            return flask.make_response(flask.jsonify({'data': data}), 201)
        except Exception as e:
            print("error: -", e)
            return flask.make_response(flask.jsonify({'error': str(e)}), 400)

    def get(self, id = None):
        """  """
        try:
            session = Session()
            fingerprint = Fingerprint(fingerprint_id=1)
            person = Person(fname="hi", fingerprints=[fingerprint])
            session.add(fingerprint)
            session.add(person)
            session.commit()

            data = list(session.query(Person).all())
            arr = []
            for x in data:
                arr.append(x.serialize())

            print(arr)
            return flask.make_response(flask.jsonify({'data': arr}), 200)
        except Exception as e:
            print("error: -", e)
            return flask.make_response(flask.jsonify({'error': str(e)}), 400)

    def put(self, id = None):
        """  """
        try:
            data = ""
            return flask.make_response(flask.jsonify({'data': data}), 200)
        except Exception as e:
            print("error: -", e)
            return flask.make_response(flask.jsonify({'error': str(e)}), 400)

    def delete(self, id = None):
        """  """
        try:
            data = ""
            return flask.make_response(flask.jsonify({'data': data}), 204)
        except Exception as e:
            print("error: -", e)
            return flask.make_response(flask.jsonify({'error': str(e)}), 400)

