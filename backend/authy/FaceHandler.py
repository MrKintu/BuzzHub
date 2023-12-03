import random
import string
from pathlib import Path
from uuid import uuid4

import torch
from PIL import Image
from transformers import DetrImageProcessor, DetrForObjectDetection
import cv2
import os
import csv
import numpy as np
import pandas as pd


def detect_face(imgPath):
    image = Image.open(imgPath).convert("RGB")

    processor = DetrImageProcessor.from_pretrained(
        "facebook/detr-resnet-50", revision="no_timm")
    model = DetrForObjectDetection.from_pretrained(
        "facebook/detr-resnet-50", revision="no_timm")

    inputs = processor(images=image, return_tensors="pt")
    outputs = model(**inputs)

    target_sizes = torch.tensor([image.size[::-1]])
    results = processor.post_process_object_detection(outputs,
                                                      target_sizes=target_sizes,
                                                      threshold=0.9)[0]

    box = []
    for score, label, box in zip(results["scores"], results["labels"],
                                 results["boxes"]):
        box = [round(i, 2) for i in box.tolist()]
        print(
            f"Detected {model.config.id2label[label.item()]} with confidence "
            f"{round(score.item(), 3)} at location {box}"
        )
    photo = image.crop(box)
    rand_strings = ''.join(random.choice(string.ascii_lowercase
                                         + string.digits
                                         + string.ascii_uppercase)
                           for i in range(5))
    file_name = f"{rand_strings}{uuid4().hex}.jpg"
    BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
    path = f'{BASE_DIR}\\media\\faces\\{file_name}'
    photo.save(path)

    return path


# Take Images is a function used for creating the sample of the images which is
# used for training the model. It takes 60 Images of every new user.
def TakeImages(name):
    Id = str(np.random.randint(1, 100))
    # Checking if the ID is numeric and name is Alphabetical
    if name.isalpha():
        # Opening the primary camera if you want to access
        # the secondary camera you can mention the number
        # as 1 inside the parenthesis
        cam = cv2.VideoCapture(0)
        # Specifying the path to haarcascade file
        BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
        harcascadePath = (f'{BASE_DIR}\\authy\\FaceData\\'
                          f'haarcascade_frontalface_default.xml')
        # Creating the classier based on the haarcascade file.
        detector = cv2.CascadeClassifier(harcascadePath)
        # Initializing the sample number(No. of images) as 0
        sampleNum = 0
        while True:
            # Reading the video captures by camera frame by frame
            ret, img = cam.read()
            # Converting the image into grayscale as most of
            # the processing is done in gray scale format
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # It converts the images in different sizes
            # (decreases by 1.3 times) and 5 specifies the
            # number of times scaling happens
            faces = detector.detectMultiScale(gray, 1.3, 5)

            # For creating a rectangle around the image
            for (x, y, w, h) in faces:
                # Specifying the coordinates of the image as well
                # as color and thickness of the rectangle.
                # incrementing sample number for each image
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                sampleNum = sampleNum + 1
                # saving the captured face in the dataset folder
                # TrainingImage as the image needs to be trained
                # are saved in this folder
                TrainingImagePath = f'{BASE_DIR}\\authy\\TrainingImage\\'
                cv2.imwrite(TrainingImagePath + name + "." + Id + '.'
                            + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
                # display the frame that has been captured
                # and drawn rectangle around it.
                cv2.imshow('frame', img)
            # wait for 100 milliseconds
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is more than 60
            elif sampleNum > 60:
                break
        # releasing the resources
        cam.release()
        # closing all the windows
        cv2.destroyAllWindows()
        # Displaying message for the user
        res = "Images Saved for ID : " + Id + " Name : " + name
        # Creating the entry for the user in a csv file
        row = [Id, name]
        UserDetailsPath = rf'{BASE_DIR}\\authy\\FaceData\\UserDetails.csv'
        with open(UserDetailsPath, 'a+') as csvFile:
            writer = csv.writer(csvFile)
            # Entry of the row in csv file
            writer.writerow(row)
        csvFile.close()

        return True
    else:
        return False


def getImagesAndLabels(path):
    # get the path of all the files in the folder
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    # creating empty ID list
    Ids = []
    # now looping through all the image paths and loading the
    # Ids and the images saved in the folder
    for imagePath in imagePaths:
        # loading the image and converting it to gray scale
        pilImage = Image.open(imagePath).convert('L')
        # Now we are converting the PIL image into numpy array
        imageNp = np.array(pilImage, 'uint8')
        # getting the Id from the image
        Id = int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces.append(imageNp)
        Ids.append(Id)
    return faces, Ids


# Training the images saved in training image folder
def TrainImages():
    # Local Binary Pattern Histogram is a Face Recognizer
    # algorithm inside OpenCV module used for training the image dataset
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    # Specifying the path for HaarCascade file
    BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
    harcascadePath = (f'{BASE_DIR}\\authy\\FaceData\\'
                      f'haarcascade_frontalface_default.xml')
    # creating detector for faces
    detector = cv2.CascadeClassifier(harcascadePath)
    # Saving the detected faces in variables
    TrainingImagePath = f'{BASE_DIR}\\authy\\TrainingImage\\'
    faces, Id = getImagesAndLabels(TrainingImagePath)
    # Saving the trained faces and their respective ID's
    # in a model named as "Trainer.yml".
    recognizer.train(faces, np.array(Id))
    TrainerPath = f'{BASE_DIR}\\authy\\FaceData\\Trainer.yml'
    recognizer.save(TrainerPath)

    return True


def TrackImages():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    # Reading the trained model
    BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
    trainer = f'{BASE_DIR}\\authy\\FaceData\\Trainer.yml'
    recognizer.read(trainer)
    harcascadePath = (f'{BASE_DIR}\\authy\\FaceData\\'
                      f'haarcascade_frontalface_default.xml')
    faceCascade = cv2.CascadeClassifier(harcascadePath)
    # getting the name from "userdetails.csv"
    user_details = f'{BASE_DIR}\\authy\\FaceData\\UserDetails.csv'
    df = pd.read_csv(user_details)
    print(df)
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            print(f'ID of {Id} with a confidence of {conf}')
            if conf > 40:
                aa = df.loc[df['Id'] == Id]['Name'].values
                tt = str(Id) + "-" + aa
            else:
                Id = 'Unknown'
                tt = str(Id)
            cv2.putText(im, str(tt), (x, y + h),
                        font, 1, (255, 255, 255), 2)
        cv2.imshow('im', im)
        if cv2.waitKey(1) == ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()

    return True
