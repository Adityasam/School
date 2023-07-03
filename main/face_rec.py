from ast import While, arg
import time
import pickle as pkl
import face_recognition
import threading
import os, io
from base64 import encodebytes
from PIL import Image, ImageOps
import shutil
import cv2
import numpy as np
#from .antispoof.test import test
from PIL import Image
from numpy import asarray
from django.core.files.storage import FileSystemStorage
from django.conf import settings as django_settings

COMMANDSFOLDER = 'COMMANDS'
FACEDATA_FOLDER = 'FACEDATA'
FACE_FOLDER = 'FACES'

def get_all_faces():
    di = FACEDATA_FOLDER
    nm = []
    for filename in os.listdir(django_settings.STATIC_ROOT+"/"+di):
        if filename.endswith(".pkl"):
            nm.append(filename)

    return nm

def get_user_photos(code):
    di = FACE_FOLDER
    nm = []
    for filename in os.listdir(django_settings.STATIC_ROOT+"/"+di):
        if code in filename:
            nm.append(filename)

    return nm

def delete_old_images(code):
    di = FACE_FOLDER
    for filename in os.listdir(django_settings.STATIC_ROOT+"/"+di):
        if code in filename:
            os.remove(django_settings.STATIC_ROOT+"/"+di+"/"+filename)

    di = FACEDATA_FOLDER
    for filename in os.listdir(django_settings.STATIC_ROOT+"/"+di):
        if code in filename:
            os.remove(django_settings.STATIC_ROOT+"/"+di+"/"+filename)

def imgtobyte(code):
    try:
        pil_img = Image.open(FACE_FOLDER+"\\"+code+".jpg", mode='r') # reads the PIL image
        byte_arr = io.BytesIO()
        pil_img.save(byte_arr, format='JPEG') # convert the PIL image to byte array
        encoded_img = encodebytes(byte_arr.getvalue()).decode('ascii') # encode as base64
        return encoded_img
    except:
        return ""

def encode_face(image_file,ename):
    returndata = "0"
    try:
        print("Encoding Started...")
        unknown_encoding = face_recognition.face_encodings(image_file)

        if len(unknown_encoding) > 0:
            fs = django_settings.STATIC_ROOT + '/'+FACEDATA_FOLDER+"/"+ ename +".pkl"
            filename = fs
            print(filename)
            with open(filename, "wb") as f:
                pkl.dump(unknown_encoding[0], f)

            filename2 = django_settings.STATIC_ROOT + '/'+FACE_FOLDER+"/"+ename+".jpg"

            image = Image.fromarray(image_file)
            image.save(filename2)
                
            print("Encoding Finished...")
            returndata = "1"
    except:
        print("Encoding Failed...")
        returndata = "0"
        pass

    return {"statuscode":returndata}
    
# def detect_real_fake(folder):
#     ret = 0
#     #img = cv2.imread(COMMANDSFOLDER+"\\"+folder+"\\temp.jpg")
    
#     img = Image.open(COMMANDSFOLDER+"\\"+folder+"\\temp.jpg")

#     w = img.width
#     h = img.height

#     img = img.resize((int(w*3/4), w))

#     numpydata = asarray(img)

#     moddir = "C:/inetpub/wwwroot/face/main/antispoof/resources/anti_spoof_models";

#     label = test(
#         image=numpydata,
#         model_dir=moddir,
#         device_id=0
#         )
        
#     if label == 1:
#         ret = 1
#     else:
#         ret = 0 

#     return ret
    
def recognize_face_image(image_file):
    name = ""
    returndata = ""
    imagebyte = ""
    try:
        print("Face Recognition Started...")
        #realfake = detect_real_fake(folder)
        realfake = 1
        if realfake == 0:
            returndata = "FAKE"
        else:
            unknown_encoding = face_recognition.face_encodings(image_file)

            if len(unknown_encoding) > 0:
                allfaces = get_all_faces()
                unknown_encoding = unknown_encoding[0]

                all_encodings = []

                for face in allfaces:
                    with open(django_settings.STATIC_ROOT+"/"+FACEDATA_FOLDER+"/"+face, "rb") as f:
                        all_encodings.append(pkl.load(f))

                results = face_recognition.compare_faces(all_encodings, unknown_encoding,tolerance=0.4)
                res = ""
                for result in results:
                    if result == True:
                        res = results.index(result)

                if res != "":
                    name = str(allfaces[res]).replace(".pkl", "").split("^")[0]
                    print("Face Recognized as : " +name)
                    returndata = name
                    imagebyte = imgtobyte(name)
                else:
                    name = "cannot"
                    print("Couldn't recognize the face")
                    returndata = "CANNOT"

            else:
                name = "noface"
                print("No Face Found In the picture")
                returndata = "NOFACE"
    except:
        name = "cannot"
        print("Face Recognition Failed...")
        returndata = "FAILED"

    return {"result":returndata, 'image':imagebyte}