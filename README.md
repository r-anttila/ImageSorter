# ImageSorter

This is a simple image sorter script that uses OpenCV face detection to sort images from a
directory to two other directories, one of which contains the images which contain faces and the other images without faces.

## Dependencies

Running the script requires the following dependencies:

- [OpenCV](https://opencv.org/)

  This can be installed using `pip install opencv-python`

- [filetype](https://github.com/h2non/filetype.py)

  This can be installed using `pip install filetype`

- [tqdm](https://github.com/tqdm/tqdm)

  This can be installed using `pip install tqdm`

## Usage

Using the script is very simple. Just run the script from your commandline. Note that you have to specify the path to your OpenCV installation
(the folder called cv2) as an argument when running the script. The arguments that the script accepts are:

- `--in_folder`
  The path to the folder you want to sort

- `--faces_folder`
  The path to the folder in which you want to move the images containing faces. Defaults to in_folder/faces

- `--no_faces_folder`
  The path to the folder in which you want to move the images which do not contain faces. Defaults to in_folder/no_faces

- `--cv_path`
  The path to your OpenCV installation (the folder called cv2)
