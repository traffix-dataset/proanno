from argparse import ArgumentParser
import os
from utils import *


if __name__ == "__main__":
    arg_parser = ArgumentParser()
    arg_parser.add_argument("--input_folder_path_drive", type=str, required=True, help="Path to the input folder")
    args = arg_parser.parse_args()
    img_dir = os.path.join(args.input_folder_path_drive, 'images')

    img_channels = os.listdir(img_dir)
    img_dirs = [i for i in img_channels if 'camera' in i]
    for dir in img_dirs:
        imgs = sorted(glob.glob(os.path.join(img_dir, dir, '*.jpg')))
        for img in imgs:
            # resize_image_by_width_height(img_path=img, width=1920, height=1200)
            resize_image_by_factor(img_path=img, size_factor=4)

