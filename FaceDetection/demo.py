import face_detection as fd
import argparse
import os.path
import cv2 as cv

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Face Detector")
    parser.add_argument('--cv_path', help='Path to cv installation.',
                        default="C:/Users/Roope/miniconda3/envs/tf/Lib/site-packages/cv2")
    parser.add_argument('--image_path', help='Path to the image', default=None)
    args = parser.parse_args()

    profileface_cascade = os.path.join(
        args.cv_path, "data\haarcascade_profileface.xml")
    frontalface_cascade = os.path.join(
        args.cv_path, "data\haarcascade_frontalface_alt.xml")

    image = cv.imread(args.image_path)

    if image is None:
        print('--(!)Error loading the image')
        exit(0)

    frontal_detector = fd.FaceDetector(frontalface_cascade)

    cv.namedWindow('Face Detector', flags=cv.WINDOW_NORMAL)

    frontal_detector.detect_and_display(image)
