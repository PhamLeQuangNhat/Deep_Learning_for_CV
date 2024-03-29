"""use python3 Chapter2/augmentation_demo.py --image datasets/jemma.png --output Chapter2/output"""

from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
import numpy as np
import argparse

def option():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True,
                    help="path to the input image")
    ap.add_argument("-o", "--output", required=True,
        help="path to output directory to store augmentation examples")
    ap.add_argument("-p", "--prefix", type=str, default="image",
                    help="output filename prefix")
    args = vars(ap.parse_args())
    return args

def main():
    args = option()

    # load the input image
    print("[INFO] loading example image...")
    image = load_img(args["image"])
    # convert it to a NumPy array
    image = img_to_array(image)
    # reshape it to have an extra dimension
    image = np.expand_dims(image, axis=0)

    # construct the image generator for data augmentation
    aug = ImageDataGenerator(rotation_range=30, width_shift_range=0.1,
            height_shift_range=0.1, shear_range=0.2, zoom_range=0.2,
            horizontal_flip=True, fill_mode="nearest")
    total = 0

    # construct the actual Python generator
    print("[INFO] generating images...")
    imageGen = aug.flow(image, batch_size=1, save_to_dir=args["output"],
                save_prefix=args["prefix"], save_format="jpg")
    
    # loop over examples from our image data augmentation generator
    for image in imageGen:
        total += 1
        if total == 10:
            break

if __name__=='__main__':
    main()
    

