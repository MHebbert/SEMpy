import cv2
import numpy as np



class Point:
    def __init__(self, x, y, area):
        self.x = x
        self.y = y
        self.area = area


  
class Sample:
    def __init__(self, photo1, photo2):
        self.photo1 = photo1
        self.photo2 = photo2
      points = []
      
  
