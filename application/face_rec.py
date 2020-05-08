import dlib
import face_recognition
import os
import cv2
from application.db import Session, Person
import base64
import numpy as np
from io import StringIO

TOLERANCE = 0.6
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = "hog"  # default: 'hog', other one can be 'cnn' - CUDA accelerated (if available) deep-learning pretrained model

def readb64(base64_string):
    sbuf = StringIO()
    sbuf.write(base64.b64decode(base64_string))
    pimg = Image.open(sbuf)
    return cv2.cvtColor(np.array(pimg), cv2.COLOR_RGB2BGR)

print('Loading known faces...')
known_faces = []
known_names = []

def initFaceRec():
    session = Session()
    # We oranize known faces as subfolders of KNOWN_FACES_DIR
    # Each subfolder's name becomes our label (name)
    for face, name in session.query(Person.face, Person.person_id).all():
            # Load an image
            nparr = np.fromstring(base64.b64decode(face), np.uint8)
            image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            
            # Get 128-dimension face encoding
            # Always returns a list of found faces, for this purpose we take first face only (assuming one face per image as you can't be twice on one image)
            encoding = face_recognition.face_encodings(image)[0]

            # Append encodings and name
            known_faces.append(encoding)
            known_names.append(name)

    session.close()

def identifyFace(image):
    print('Identifying Face')
    nparr = np.fromstring(base64.b64decode(image), np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    #image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    locations = face_recognition.face_locations(image, model=MODEL)
    encodings = face_recognition.face_encodings(image, locations)

    res = {}

    for face_encoding, face_location in zip(encodings, locations):
        results = face_recognition.face_distance(known_faces, face_encoding)
        res = {known_names[i]: results[i] for i in range(0, len(results)) }
    
    return res

def identifyFaceVideo(url):
    video = cv2.VideoCapture(url)
    image = video.read()[1]
    ret, image = cv2.imencode(".png", image)
    
    nparr = np.fromstring(image, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    locations = face_recognition.face_locations(image, model=MODEL)
    encodings = face_recognition.face_encodings(image, locations)

    face_locations = {} #face locations to be drawn

    for face_encoding, face_location in zip(encodings, locations):
        
        face_locations.update(compareFace(face_encoding, face_location))

    for k, v in face_locations.items():
        # Paint frame
        cv2.rectangle(image, v[0], v[1], [255, 0, 0], FRAME_THICKNESS)
        # Wite a name
        cv2.putText(image, k, v[0], cv2.FONT_HERSHEY_SIMPLEX, 1.5, [255, 0, 255], FONT_THICKNESS)

        # Show image
    image = cv2.imencode(".jpg", image)[1]
    return image


def compareFace(face_encoding, face_location):
    results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
    face_locations = {}
    match = None
    if True in results:  # If at least one is true, get a name of first of found labels
        match = "name"
        print(f' - {match} from {results}')
        top_left = (face_location[3], face_location[0])
        bottom_right = (face_location[1], face_location[2])

        face_locations[match] = (top_left, bottom_right)
    return face_locations