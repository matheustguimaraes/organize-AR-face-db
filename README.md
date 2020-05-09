# Organize [AR Face Database](http://www2.ece.ohio-state.edu/~aleix/ARdatabase.html)

Scripts to organize the AR Face Database
1. Transform .raw files to .jpeg images
2. Create folders to store separate images in classes
3. Separate images in train, scarf and glass folders

## Motivation
The scripts were created to prepare different configurations of
images in each class, number of folders, section of images, size of class, etc... Doing
all different configurations without scripts would require a large amount of time just to
prepare the database.

## Prerequisites
1. Download and install [ImageMagick](https://imagemagick.org/index.php)
2. Create a virtual environment
```shell script
sudo apt-get install python3-venv
python3 -m venv .env
source .env/bin/activate
```

## Scripts
### Convert .raw files to .jpeg
``` 
python organize/raw2jpeg.py \
    -d databases/dbf1
```

### Create 134 folders at once
``` 
python organize/create_folders.py \
    -p databases/AR/train \
    -i 0 \
    -e 134
```

### Store 4 images of each person in a folder
Example: Dataset first session:
```
python organize/images2folders.py \
    -a databases/AR/all_images \
    -f databases/AR/valid_folders \
    -s 1
```

### Standardize image filenames
Each image will have a name from 0.jpeg to 3.jpeg
``` 
python organize/rename_files.py \
    -d databases/AR/valid_folders
```

## Disclaimer
I do not own the AR Face Database or have any connection with his owners. 
To download a copy of the dataset, you must follow the instructions on his 
official website: 
[AR Face Database](http://www2.ece.ohio-state.edu/~aleix/ARdatabase.html)
