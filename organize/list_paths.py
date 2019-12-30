"""
List all files with chosen type

Source code modified from imutils package (https://github.com/jrosebr1/imutils)
Original file: https://github.com/jrosebr1/imutils/blob/master/imutils/paths.py
"""

import os


def list_files(base_path, valid_exts=None, contains=None):
    """ Return the set of files with a given extension in a path """
    # loop over the directory structure
    for (rootDir, dirNames, filenames) in os.walk(base_path):
        # loop over the filenames in the current directory
        for filename in filenames:
            # if the contains string is not none and the filename does not
            # contain the supplied string, then ignore the file
            if contains is not None and filename.find(contains) == -1:
                continue

            # determine the file extension of the current file
            ext = filename[filename.rfind("."):].lower()

            # check to see if the file is an image and should be processed
            if valid_exts is None or ext.endswith(valid_exts):
                # construct the path to the image and yield it
                image_path = os.path.join(rootDir, filename)
                yield image_path
