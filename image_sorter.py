import face_detection as fd
import os
import pathlib as path
import cv2 as cv
import argparse
import filetype as ft
from tqdm import tqdm


def create_output_folder(p):
    if isinstance(p, path.Path):  # If the default output folder path is used
        folder = os.path.join(in_folder, p)
    else:
        folder = os.path.abspath(p)  # Use the absolute path if it is specified
    return folder


# Create an argument parser to read input from command line
parser = argparse.ArgumentParser(
    description='A python script that sorts images from a folder to two folders, one containing photos with faces and other those without faces')
parser.add_argument('--in_folder', help="The path to the folder you want to sort. Default is current folder.",
                    default=path.Path())
parser.add_argument('--faces_folder', help="The path to the folder where the images with faces are stored. Default is in_folder/faces.",
                    default=path.Path('faces'))
parser.add_argument('--no_faces_folder', help="The path to the folder where the images without faces are stored. Default is in_folder/no_faces.",
                    default=path.Path('no_faces'))
parser.add_argument('--cv_path', help='The path to the folder containing the cv2 installation',
                    default="C:/Users/Roope/miniconda3/envs/tf/Lib/site-packages/cv2")
args = parser.parse_args()

# Get the Path objects to the input and output folders
in_folder = os.path.abspath(args.in_folder)
faces_folder = create_output_folder(args.faces_folder)
no_faces_folder = create_output_folder(args.no_faces_folder)


# Create the directories if they dont exist
os.makedirs(in_folder, exist_ok=True)
os.makedirs(faces_folder, exist_ok=True)
os.makedirs(no_faces_folder, exist_ok=True)


# Get the contents of the input directory
images = os.scandir(in_folder)

# Getting the profile and frontal cascades from the cv2 library
profileface_cascade = os.path.join(
    args.cv_path, "data\haarcascade_profileface.xml")
frontalface_cascade = os.path.join(
    args.cv_path, "data\haarcascade_frontalface_alt.xml")

# Creating two face detectors, one for detecting full frontal faces and one for profiles
# For best result we combine results from both detectors to check for faces
frontal_detector = fd.FaceDetector(frontalface_cascade)
profile_detector = fd.FaceDetector(profileface_cascade)

# Only sort files that are images
print("Identifying images...")
images = [image for image in images if image.is_file()
          and ft.is_image(image.path)]

if not images:  # Exit the program if no images are found
    print("No Images found in the given folder.")
    exit()

for image in tqdm(images, desc="Sorting pictures"):
    try:
        cv_image = cv.imread(image.path)
    except:
        continue  # In case of an error in reading the picture we just skip sorting the picture

    if frontal_detector.contains_face(cv_image) or profile_detector.contains_face(cv_image):
        dest_path = os.path.join(faces_folder, image.name)
    else:
        dest_path = os.path.join(no_faces_folder, image.name)

    os.rename(image.path, dest_path)

print("All images sorted")
