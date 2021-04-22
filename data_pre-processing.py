from __future__ import division
import numpy as np
import imageioi
mport mathi
mport matplotlib.pyplot as plt
from skimage.transform import resize
from skimage.io import imread
import tensorflow as tf
from skimage import transform
from PIL import Image

import imageio
import shutil
import scipy.misc
import os
import pandas as pd

def sort_images(csv_file):
    c = 0
    df = pd.read_csv(os.getcwd() + '/' + csv_file)
    image_column = df.path                                  # contain the name of the user specific genre image 'eg -abc.jpg'
    os.mkdir(os.getcwd() + '/data/train_9_landscape')
    for i in image_column:
    try:
        shutil.move(os.getcwd() + '/data/train_9/' + str(i), os.getcwd() + '/data/train_9_landscape') #move img(all genres) from a folder to img (usr choice genre) to another folder
        c = c+1
    except:
        print('pic not there')
    return c

def prepare_data(folder_name, resize_ht, resize_wt):
    image_path = os.getcwd() + '/data/' + folder_name
    file_images = os.listdir(image_path)
    os.mkdir(os.getcwd() + '/data/discarded_images')
    os.mkdir(os.getcwd() + '/data/resized_images')
    for i in file_images:
        image = imageio.imread(image_path + '/' + i)
        if len(image.shape) != 3 or image.shape[-1] != 3:  # check for color or gray scale ; remove ifgrayscale
            shutil.move(image_path + '/' + i, os.getcwd()+'/data/discarded_images')
            print('%i Image Moved', i)
        else:
            resize_image = resize(image, [resize_ht, resize_wt])
            data = 255 * resize_image  # Now scale by 255
            img = data.astype(np.uint8)
            imageio.imsave(os.getcwd() + '/data/resized_images/' + i, img, format='jpeg')


# FIRST RUN THIS FUNCTION# count = sort_images('landscape_9.csv') # csv contains column(named path) with all image names#
# print(count)
# SECOND RUN THIS FUNCTION
# prepare_data('train_9_landscape', 128, 128) # name of folder containing images to be resized