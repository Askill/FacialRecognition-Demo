import dlib
import face_recognition
import os
import cv2
from application.db import Session, Person
import base64
import numpy as np
from io import StringIO
import application.config as config

TOLERANCE = config.tolerance
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = config.model  # default: 'hog', other one can be 'cnn' - CUDA accelerated (if available) deep-learning pretrained model

known_faces = []
known_names = []

def initFaceRec() :
    ''' Initializes Facial recognition with faces in current db  '''

    print('LOADING known faces...')
    session = Session()
    for face, name in session.query(Person.face, Person.person_id).all():
        # Load an image
        nparr = np.fromstring(base64.b64decode(face), np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        # Get 128-dimension face encoding
        encoding = face_recognition.face_encodings(image)
        if len(encoding) >= 1:
            encoding = face_recognition.face_encodings(image)[0]
        else:
            continue

        # Append encodings and name
        known_faces.append(encoding)
        known_names.append(name)


    print('DONE Loading known faces...')
    session.close()

def identifyFace(image):
    print('Identifying Face')
    res = {}
    try:
        nparr = np.fromstring(base64.b64decode(image), np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        locations = face_recognition.face_locations(image, model=MODEL)
        encodings = face_recognition.face_encodings(image, locations)

        # res is the return object key: name, value: matching score
        
        count = 0
        for face_encoding, face_location in zip(encodings, locations):
            
            results = face_recognition.face_distance(known_faces, face_encoding)
            res = {known_names[i]: results[i] for i in range(0, len(results)) }
            count += 1
            print(count)
    except:
        print("error")
    return res

def identifyFaceVideo(video):
    video = video.video
    # allways get new latest image from url
    image = video.read()[1]
    #scale
    image = cv2.resize(image,None,fx=config.scaleInput,fy=config.scaleInput)
    ret, image = cv2.imencode(".png", image)
    
    #convert image to format readable by face_recognition lib
    nparr = np.fromstring(image, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    locations = face_recognition.face_locations(image, model=MODEL)
    encodings = face_recognition.face_encodings(image, locations)

    face_locations = {} #face locations to be drawn

    # can be multithreaded here
    # compares each face against all faces in DB
    for face_encoding, face_location in zip(encodings, locations):
        try:
            face_locations.update(compareFace(face_encoding, face_location))
        except Exception as e:
            print(e)

    session = Session()
    # marks faces and retrives faces by id
    for k, v in face_locations.items():
        try:
            # Paint frame
            cv2.rectangle(image, v[0], v[1], [255, 0, 0], FRAME_THICKNESS)
            # Wite a name
            name = " ".join(session.query(Person.fname, Person.lname).filter(Person.person_id == int(k)).first())
            cv2.putText(image, name, v[0], cv2.FONT_HERSHEY_SIMPLEX, 1.5, [255, 0, 255], FONT_THICKNESS)
        except Exception as e:
            print(e)
    session.close()
    image = cv2.imencode(".jpg", image)[1]
    return image


def compareFace(face_encoding, face_location):
    ''' return dict with locations and id of person '''
    results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
    face_locations = {}
    match = None
    if True in results:  # If at least one is true, get a name of first of found labels
        match = known_names[results.index(True)]
        top_left = (face_location[3], face_location[0])
        bottom_right = (face_location[1], face_location[2])

        face_locations[str(match)] = (top_left, bottom_right)
    return face_locations