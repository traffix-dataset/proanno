from argparse import ArgumentParser
import os
from utils import *


if __name__ == "__main__":

    img_dir = '/Users/ahmad/Desktop/RCI/Thesis/02_Workspace/proanno/input/Traffix/drive_33_north_to_south/images'
    img_channels = os.listdir(img_dir)
    img_dirs = [i for i in img_channels if 'camera' in i]
    for dir in img_dirs:
        imgs = sorted(glob.glob(os.path.join(img_dir, dir, '*.jpg')))
        for img in imgs:
            # resize_image_by_width_height(img_path=img, width=1920, height=1200)
            resize_image_by_factor(img_path=img, size_factor=4)

