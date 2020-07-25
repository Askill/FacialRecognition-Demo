import cv2
import base64
import application.config as config
import numpy as np

#  provides the function used for the live streams
class VideoCamera(object):
    """Video stream object"""
    url = config.videoSource
    
    def __init__(self):
        if  isinstance(self.url, int):
            self.video = cv2.VideoCapture(self.url, cv2.CAP_DSHOW)
        else:
            self.video = cv2.VideoCapture(self.url)

    def __del__(self):
        self.video.release()
    
    def recap(self):
        
        self.video = cv2.VideoCapture(self.url)

    def get_frame(self, ending):
        self.recap()
        success, image = self.video.read()
        if image is None:
            image = np.zeros((100,100,3), np.uint8)
        ret, jpeg = cv2.imencode(ending, image)
        return jpeg
        
    def get_frame2(self, ending):

        success, image = self.video.read()
        return image
