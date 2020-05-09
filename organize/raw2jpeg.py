"""
Convert files from .raw to .jpeg format and store in defined folder.
To successfully run this code, ImageMagick must be installed in your system

ImageMagick installation:
    sudo apt-get update
    sudo apt install imagemagick

Usage:
python raw2jpeg.py --dataset ds/AR_raw/ --save ds/AR_jpeg/

TODO: Convert this code to bash script
"""

import os
from argparse import ArgumentParser
from sys import argv

from organize import list_paths as lp


def convert_raw(list_args):
    # Construct the argument parser
    ap = ArgumentParser()
    ap.add_argument("-i", "--dataset", required=True,
                    help="path to AR dataset in .raw format")
    ap.add_argument("-s", "--save", required=False,
                    help="path to save images")
    args = ap.parse_args(list_args)

    # Set a path to save the images in jpeg, if you want.
    # If not pass the --save argument, the jpeg images will be saved in the
    # same folder of .raw images
    ds = args["dataset"]
    save_path = args["save"]

    if args["save"]:
        save_path = save_path
    else:
        save_path = os.path.dirname(ds)

    # List dataset images
    image_paths = list(lp.list_files(ds, valid_exts='.raw'))

    # ImageMagick command to convert from .raw to .jpeg
    convert = 'convert -depth 8 -interlace plane -size 768x576'

    # Loop over the image paths
    for i, path in enumerate(image_paths):
        print("[INFO] Converting image {}".format(i + 1))
        img_folder = path.replace(ds, '').replace('.raw', '.jpeg')

        # Check if folder exists, if not, create folder
        created_folder = os.path.join(save_path, os.path.dirname(img_folder))
        os.makedirs(created_folder, exist_ok=True)

        # Convert using ImageMagick and store all images in defined folder
        os.system('{} rgb:{} {}{}'.format(convert, path, save_path,
                                          img_folder))


if __name__ == '__main__':
    convert_raw(argv)
