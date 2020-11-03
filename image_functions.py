from PIL import Image
import os
import tensorflow as tf
import numpy as np


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
    return "True"

def convert_to_numpy(dirpath):
    onlyfiles = [f for f in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, f))]
    print(onlyfiles)
    x = np.array([np.array(Image.open(dirpath+"/"+fname)) for fname in onlyfiles])
    print(x)
    return "True"
