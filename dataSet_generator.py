import cv2

#just a shortcut
import numpy as np

import sqlite3

#using defualt haarcascade from opencv library (opencv->sources->data->haarcascades)

#calling cascade classifier with file name with file extension
faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');

#video capture object to capture images for webcam value (video capture id) is 0 or else try 1
cam = cv2.VideoCapture(0);

#capture frames one by one and detect faces and show them in a window

def insertOrUpdate(id,name):
    conn =sqlite3.connect("facedatabase.db");
    cmd = "SELECT * FROM details WHERE id="+str(id);
    cursor =conn.execute(cmd);
    isRecordExist = 0;
    for row in cursor:
        isRecordExist = 1;
    if(isRecordExist ==1):
        cmd ="UPDATE details SET name="+str(name)+" WHERE id="+str(id);
    else:
        cmd ="INSERT INTO details(id,name) Values("+str(id)+","+str(name)+")";
    conn.execute(cmd);
    conn.commit();
    conn.close();
    
#write the face into folder whenever it captures using identifier
id = raw_input('Enter User ID: ');
name = raw_input('Enter User Name: [Note: within quotes]');
insertOrUpdate(id,name);
#sample number to keep count
sampleNum = 0;

#creating loop and braking it with key
while(True):
    ret,img = cam.read();
    #returns status variable and one captured image

    #for classifier to work converting color image into grayscale one
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY);

    #list to store the faces
    faces = faceDetect.detectMultiScale(gray,1.3,3,5);
    #this will detect all the faces in the frames and return co-ordinates of the faces in the frame

    #we can get multiple f(x+waces so drawing rectangles around faces
    for(x,y,w,h) in faces:

        sampleNum = sampleNum+1;
        #writing captures faces in a folder with custom file name with id and number with input image
        cv2.imwrite("dataSet/User."+str(id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w]);
        
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2);
        # parameters variablles, starting point, ending point, BGR, width

        #100ms delay
        cv2.waitKey(100);

    #displaying the faces
    cv2.imshow("Face",img);

    #wait command or else it wont work
    cv2.waitKey(1);

    #exit on sample number higher than 2 so we get 3 samples
    if(sampleNum>2):
        break;
    
#freeing up camera
cam.release();

#closing all windows
cv2.destroyAllWindows();

        
    
    
