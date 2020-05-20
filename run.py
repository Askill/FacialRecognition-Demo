from application import app
from application.face_rec import initFaceRec
import application.config as config

initFaceRec()
app.run(host="localhost", port=config.port, debug=config.debug, threaded=True)



