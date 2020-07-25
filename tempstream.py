from flask import Flask, request, Response
import cv2
from time import sleep
app = Flask(__name__)


class VideoCamera(object):
    """Video stream object"""
    url = "./example.mp4"
    def __init__(self):
        self.video = cv2.VideoCapture(self.url)

    def __del__(self):
        self.video.release()
    
    def get_frame(self, ending):
        success, image = self.video.read()
        ret, jpeg = cv2.imencode(ending, image)
        sleep(.023)
        return jpeg

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame('.jpg').tobytes()
        yield (b'--frame\r\n'
       b'Content-Type:image/jpeg\r\n'
       b'Content-Length: ' + f"{len(frame)}".encode() + b'\r\n'
       b'\r\n' + frame + b'\r\n')

@app.route("/1.mjpeg")
def webhook():
    return Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, threaded=True, debug=False)