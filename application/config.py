
# Database config
databaseFile = "./test.sqlite"
echoDatabase = False


# Web Server config
debug = True
port = '5001'


# Face recognition config
model = "hog" # can be hog or cnn
tolerance = 0.6
useCUDA = True # is only relevant if dlib installer glitched out during installatzion
videoSource = "http://192.168.178.56:8080/video" # used by openCV, can use webcams or videostreams

