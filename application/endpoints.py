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
            jsonData = flask.request.get_json(force=True)
            personJSON = jsonData["person"]

            session = Session()
            fingerprintsObj = []
            for fingerprint in personJSON["fingerprints"]:
                fingerprint["fingerprint"] = fingerprint["fingerprint"].encode('utf-8')
                fp = Fingerprint(**fingerprint) # ** Operator converts DICT/JSON to initializable 
                fingerprintsObj.append(fp)  
                session.add(fp)

            personJSON["fingerprints"] = fingerprintsObj
            personJSON["face"] = personJSON["face"].encode('utf-8')
            person = Person(**personJSON)
            session.add(person)
            session.commit()

            data = list(session.query(Person).filter_by(person_id=person.person_id))
            arr = []
            for x in data:
                arr.append(x.serialize())

            return flask.make_response(flask.jsonify({'data': arr}), 201)

        except Exception as e:
            print("error: -", e)
            return flask.make_response(flask.jsonify({'error': str(e)}), 400)

    def get(self, id = None):
        """  """
        try:
            session = Session()
            if id is None:
                data = list(session.query(Person).all())
            else:
                data = list(session.query(Person).filter_by(person_id=id))
            arr = []
            for x in data:
                arr.append(x.serialize())

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

