from application import app
from application.face_rec import initFaceRec
initFaceRec()
app.run(host="localhost", port='5001', debug=True)



