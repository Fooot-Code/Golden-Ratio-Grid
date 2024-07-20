import cv2

class Rectangle:
    def __init__(self, startPosition, startingWidth, startingHeight):
        self.self = self
        self.startPosition = startPosition
        self.startingWidth = startingWidth
        self.startingHeight = startingHeight
    
    def draw(self):
        rectangleLocation = ((self.startPosition[0], self.startPosition[1]), (self.startPosition[0] + self.startingWidth, self.startPosition[1] + self.startingHeight))
        return rectangleLocation

def width_to_height(width):
    height = phi * width - width
    return height

image = cv2.imread("BaseImage.png")
imageWidth, imageHeight, _ = image.shape
startingWidth = 0.5
startingHeight = width_to_height(startingWidth)
phi = 1.61803398874

rectangleList = []

for x in imageWidth:
    for y in imageHeight:
        if len(rectangleList) > 0:
            rectangleList[-1][1]

