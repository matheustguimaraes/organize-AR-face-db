"""
Rename all images from 0.jpeg to n.jpeg, inside each class and folder

Example:
After this script, the train classes are renamed to the following pattern:
    ds/tr_gl_sc/train/0/0.jpeg
    ds/tr_gl_sc/train/0/1.jpeg
    ds/tr_gl_sc/train/0/2.jpeg
    ds/tr_gl_sc/train/0/3.jpeg

Usage:
python organize/rename_files.py -d datasets/tr_gl_sc/
"""

import argparse
from os import system

from organize import list_paths as lp

# Construct the argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
                help="path to input directory of files")
args = vars(ap.parse_args())

# Dataset path to train/test folders
dataset = args["dataset"]

# List dataset images
img_paths = list(lp.list_files(args["dataset"], valid_exts='.jpeg'))
paths_list = [k.replace('.jpeg', '').replace('-', ' ').replace('/', ' ').split(' ') for k in img_paths]

n_train = n_test = 0
for i, path in enumerate(paths_list):
    # Get folders in path list
    path_folder = path[0:4]
    # Create string to pass as destination folder
    path_str = "/".join(path_folder)

    # Create image name by number of images in each class
    # Train folders have 4 images each in each class
    if path_folder[2] == 'train':
        system('mv {} {}/{}.jpeg'.format(img_paths[i], path_str, n_train))
        n_train += 1 if n_train < 3 else 0

    # Glass and Scarf folders have 3 images in each class
    elif path_folder[2] == 'glass' or path_folder[2] == 'scarf':
        system('mv {} {}/{}.jpeg'.format(img_paths[i], path_str, n_test))
        n_test += 1 if n_test < 2 else 0
