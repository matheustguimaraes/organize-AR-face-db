"""
Copy images to folders

This script is used to organize AR dataset in train, scarf and glass, and
separate the two sessions from dataset
eg. one folder for train and two for test, from each session folder

Usage:
python organize/images2folders.py \
    -d datasets/AR_jpeg/ \
    -f datasets/tr_gl_sc/ \
    -s 1
"""

from argparse import ArgumentParser
from os import system
from sys import argv

from organize import list_paths as lp


def image2folders(list_args):
    # Construct the argument parser
    ap = ArgumentParser()
    ap.add_argument("-d", "--dataset", required=True,
                    help="input all images folder path")
    ap.add_argument("-f", "--folder", required=True,
                    help="path to folder with train/test images")
    ap.add_argument("-s", "--session", required=True,
                    help="type '1' or '2', for fist or second session of dataset")
    args = ap.parse_args(list_args)

    # Dataset path to all images
    ds = args["dataset"]
    # Path to folder with validation images
    folder = args['folder']
    # Session, the AR database has two sessions
    session = int(args['section'])

    # List dataset images
    img_paths = list(lp.list_files(ds, valid_exts='.jpeg'))
    paths_list = [i.replace(ds, '').replace('.jpeg', '').replace('-', ' ').split(' ') for i in img_paths]

    for i, path in enumerate(paths_list):
        # Photos that begin from 0 to 13
        if session == 1:
            division = 0
        # Photos that begin from 14 to 26
        elif session == 2:
            division = 13
        # Session not defined
        else:
            raise ValueError('The session was not defined in args, '
                             'one of three folders must be defined: '
                             'train, scarf or glass')

        path[1] = int(path[1])
        path[2] = int(path[2])
        path_fold = path[1] - 1
        # If women, store images in 75-133 folders
        path_temp = path_fold
        if path[0] == 'w':
            path_temp += 75

        print('[INFO] Copying image:', img_paths[i])
        # Copy to train folder
        if division < path[2] < division + 5:
            system('cp {} {}train/{}/'.format(img_paths[i], folder, path_temp))
        # Copy to scarf folder
        elif division + 10 < path[2] < division + 14:
            system('cp {} {}scarf/{}/'.format(img_paths[i], folder, path_temp))
        # Copy to glass folder
        elif division + 7 < path[2] < division + 11:
            system('cp {} {}glass/{}/'.format(img_paths[i], folder, path_temp))


if __name__ == '__main__':
    image2folders(argv)
