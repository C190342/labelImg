import os
from PIL import Image
import sys

# 
# This will take in a folder of images and resize all the images in that folder to where
# the largest side of the image is the max size that the user entered
# 
# This script is seperate from the other object detect scripts, however, it could be useful when trying to shrink image
# size to reduce memory usage
# 

print("Enter the path to the folder containing the images you want to re-size")
folder_holding_orig_images = input("Path: ").replace("'", "").strip()
max_size = int(input("Enter the max pixel size of the image (ex: 1024): "))

folder_for_resized_images = "new_" + str(max_size) + "_images"
os.chdir(folder_holding_orig_images)

link_create = folder_holding_orig_images + os.sep + folder_for_resized_images

def yes_no_input(max_size,link_create):
    while True:
        choice = input("Images with size of " + str(max_size)+"px will be to create in "+ link_create +" folder. 'yes' or 'no' [y/N]: ").lower()
        if choice in ['y', 'ye', 'yes']:
              return True
        elif choice in ['n', 'no']:
            return False
        
if yes_no_input(max_size,link_create):
    if not os.path.exists(folder_holding_orig_images + os.sep + folder_for_resized_images):
        # If an XML folder does not already exist, make one
        os.mkdir(folder_for_resized_images)

    print("Updating image sizes, this may take a while, enjoy some quiet time while you wait...")
    for each_image_file in os.listdir(folder_holding_orig_images):
        if each_image_file.endswith("jpg") or each_image_file.endswith("jpeg") or each_image_file.endswith("png"):
            orig_img = Image.open(each_image_file)
            new_file_path = os.path.join(folder_for_resized_images, each_image_file)
            aspect_ratio = orig_img.width / orig_img.height

            if orig_img.width > orig_img.height:
                new_width = max_size
                new_height = int(new_width / aspect_ratio)
            if orig_img.height > orig_img.width:
                new_height = max_size
                new_width = int(new_height * aspect_ratio)

            new_image = orig_img.resize((new_width, new_height))

            new_image.save(new_file_path)

    print("Image size update complete in: " + folder_holding_orig_images + os.sep + folder_for_resized_images+" folder.")
else:
    print("Application has stopped working without re-size image.")
