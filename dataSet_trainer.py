import cv2

#relative path of dataset and all images in it
import os

#just a shortcut
import numpy as np

#importing pillow library as we are capturing the images
from PIL import Image

#creating recognizer
recognizer = cv2.createLBPHFaceRecognizer();

#for relative path of our datasets along with its corresponding sub-levels with ids
path = 'dataSet'

#to get all images in their corresponding levels with ids by creating a method
def getImagesWithID(path):
    #creating a list for all the images available in that folder
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)];

    faces =[];
    IDs = [];

    for imagePath in imagePaths:
        #opening image and gray scaling
        faceImg = Image.open(imagePath).convert('L');

        #converting PIL image into Numpy array opencv only understand array numbers
        faceNp = np.array(faceImg,'uint8');
        #format unsigned integer 8

        #splitting path for file name and splitting further for ID
        ID = int(os.path.split(imagePath)[-1].split('.')[1]);

        faces.append(faceNp);
        IDs.append(ID);

        cv2.imshow("Training Image", faceNp);
        cv2.waitKey(100);

    return np.array(IDs), faces;

Ids, faces = getImagesWithID(path);
recognizer.train(faces,Ids);
recognizer.save('recognizer/trainingdata.yml');
cv2.destroyAllWindows();

        
