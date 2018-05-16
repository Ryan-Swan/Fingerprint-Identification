from model import who_is_it, create_encoding, sess, retrain
from actioncable.connection import Connection
from actioncable.subscription import Subscription
from actioncable.message import Message
import numpy as np
import scipy.misc
import re
import base64
from imageio import imread
import cv2
from skimage.transform import resize
from os import rename
connection = Connection(url='ws://localhost:3000/cable', origin='http://localhost:3000')
connection.connect()
subscription = Subscription(connection, identifier={'channel':'FaceChannel'})
image_dir_path = "./data/images"
database = retrain()
def on_receive(message):
    global database
    database = retrain()
    print(database.keys())
    message = message['message']
    print("Message: ", message)
    if re.match("Recieved faceprint: ", message):
        img_data = message.split(": ")[1]
        image_path  = image_dir_path + "/new.jpg"
        with open(image_path, "wb") as fh:
            fh.write(base64.b64decode(img_data))
            scipy.misc.imsave(image_path, align_image(image_path))
        user = who_is_it(sess, database, image_path)
        if user:
            print("Face: ", user)
            subscription.send(Message(action="authenticate", data={"message": "Face: " + user})) 
        else:
            print("Not recognised")
            subscription.send(Message(action="authenticate", data={"message": "Not recognised"}))

    if re.match('Register face: ', message):
        

        img_data = re.sub(r'Register face: (\w)*...', '', message)
        username = message.split()[2]
        image_path  = image_dir_path + "/"+ "new" + ".jpg"
        with open(image_path, "wb") as fh:
            fh.write(base64.b64decode(img_data))
            scipy.misc.imsave(image_path, align_image(image_path))
        rename(image_dir_path + "/"+ "new" + ".jpg", image_dir_path + "/"+ username + ".jpg")

def align_image(filepath, margin = 10, image_size = 96):
    cascade_path = "/Users/hassan-alubeidi/keras-facenet/model/cv2/haarcascade_frontalface_alt2.xml"
    cascade = cv2.CascadeClassifier(cascade_path)
    img = imread(filepath)
    (x, y, w, h) = cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=3)[0]
    cropped = img[y-margin//2:y+h+margin//2, x-margin//2:x+w+margin//2, :]
    aligned = resize(cropped, (image_size, image_size), mode='reflect')
    return aligned

subscription.on_receive(callback=on_receive)
subscription.create()