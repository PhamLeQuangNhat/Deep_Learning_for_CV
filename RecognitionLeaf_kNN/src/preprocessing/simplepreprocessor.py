import cv2

class SimplePreprocessor:
    def __init__(sefl, width, height, inter=cv2.INTER_AREA):
        # store the target image width, height, interpolation 
        # method used when resizing
        self.width = width
        self.height = height
        self.inter = inter
    
    def preprocess(self, image):
        # resize the image to a fixed size, ignor aspect ratio
        return cv2.resize(image, (self.width, self.height), interpolation=self.inter)
