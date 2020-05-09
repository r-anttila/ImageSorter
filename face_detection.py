import cv2 as cv


class FaceDetector(object):
    def __init__(self, xml_path):
        self.classifier = cv.CascadeClassifier(xml_path)

    def detect(self, image, biggest_only=True):
        image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        image_gray = cv.equalizeHist(image_gray)

        scale_factor = 1.2
        min_neighbors = 5
        min_size = (30, 30)
        faces_coord = self.classifier.detectMultiScale(
            image, scaleFactor=scale_factor, minNeighbors=min_neighbors, minSize=min_size)

        return faces_coord

    def contains_face(self, image):
        return True if len(self.detect(image)) > 0 else False

    def detect_and_display(self, image):
        faces_coord = self.detect(image, biggest_only=False)

        for (x, y, w, h) in faces_coord:
            lower = (x, y)
            upper = (x+w, y+h)

            image = cv.rectangle(image, lower, upper, (0, 255, 0), 10)

        cv.imshow('Face Detector', image)
        print("Press any key to close the window")
        cv.waitKey(0)
