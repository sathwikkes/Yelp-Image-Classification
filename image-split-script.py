import glob
#import cv2
import os
import shutil
#photo_folder = glob.glob("/Users/sathwikthecreator/Desktop/projects/image-classification/data/photos/")
#my_list=[]

path = "/Users/sathwikthecreator/Desktop/projects/image-classification/data/yelp_photos/"


print("Before moving file:")  
source = "/Users/sathwikthecreator/Desktop/projects/image-classification/data/yelp_photos/photos/"
destination = "/Users/sathwikthecreator/Desktop/projects/image-classification/data/yelp_photos/rand_pics2/"

#photos = os.listdir(photo_folder)

files = os.listdir(source)

for photo in files[0:2000]:
    print("moving..", photo)  
    if os.path.splitext(photo)[1] in (".jpg", ".gif", ".png"):
         shutil.move(source+photo, destination)
    print("Finished moving..")
