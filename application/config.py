
# Database config
databaseFile = "./test.sqlite"
echoDatabase = False


# Web Server config
debug = True
port = '5001'


# Face recognition config
model = "cnn" # can be hog or cnn
tolerance = 0.7
useCUDA = True # is only relevant if dlib installer glitched out during installatzion
videoSource = 0
#videoSource = "http://192.168.178.56:8080/video" # used by openCV, can use webcams or videostreams
scaleInput = 0.6
