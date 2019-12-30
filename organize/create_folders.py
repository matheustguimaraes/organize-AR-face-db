"""
Create various folders in a row, later used to store
the same people in a folder (class)

The AR dataset has 134 different people

Usage:
    python organize/create_folders.py -p datasets/AR/train/ -i 0 -e 134
"""

from argparse import ArgumentParser
from os import system
from sys import argv


def create_folders(list_args):
    # Construct the argument parser
    ap = ArgumentParser()
    ap.add_argument("-p", "--path", required=True,
                    help="initial folders value")
    ap.add_argument("-i", "--ini-folder", required=True,
                    help="initial folders value")
    ap.add_argument("-f", "--fin-folder", required=True,
                    help="final folders value")
    args = ap.parse_args(list_args)

    path = args["path"]
    ini_folder = int(args["ini_folder"])
    fin_folder = int(args["fin_folder"])

    # Create various folders in a row
    for i in range(ini_folder, fin_folder):
        system('mkdir {}{}'.format(path, str(i)))


if __name__ == '__main__':
    create_folders(argv)
