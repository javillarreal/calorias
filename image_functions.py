from PIL import Image
from flask import jsonify
import os
import tensorflow as tf
import numpy as np
import io
from base64 import encodebytes


def resize_image(input, destpath, filename):
    im = Image.open(input)
    newsize = (960, 960)
    im1 = im.resize(newsize)
    new_location = destpath + filename
    im1.save(os.path.join(destpath,filename))
    return im1


def crop_images(path, input, height, width, k, page, area, string):
    image = Image.open(input)
    newsize = (960, 960)
    im = image.resize(newsize)
    #im.save(os.path.join(path,string))
    print("loaded image")
    imgwidth, imgheight = im.size
    if imgwidth < 960 or imgheight < 960:
        return False
    else:
        for i in range(0,imgheight,height):
            for j in range(0,imgwidth,width):
                box = (j, i, j+width, i+height)
                a = im.crop(box)
                print("cropped")
                #o = a.crop(area)
                print("try saving the image")
                a.save(os.path.join(path,string+"-IMG-%s.jpg" % k))
                print("saved image")
                k +=1
        return True

def get_images(dirpath):
    onlyfiles = [f for f in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, f))]
    #encoded_images = []
    #filenames = []
    all_info = []
    for fname in onlyfiles:
        pil_img = Image.open(os.path.join(dirpath,fname), mode='r')
        byte_arr = io.BytesIO()
        pil_img.save(byte_arr, format='JPEG')
        encoded_img = encodebytes(byte_arr.getvalue()).decode('ascii')
        #encoded_images.append(encoded_img)
        #filenames.append(fname)
        all_info.append({'name': fname, 'img': encoded_img})
    return all_info

def convert_to_numpy(dirpath):
    onlyfiles = [f for f in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, f))]
    print(onlyfiles)
    x = np.array([np.array(Image.open(dirpath+"/"+fname)) for fname in onlyfiles])
    print(x)
    return "True"
