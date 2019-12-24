#!/bin/bash

: '
Create various folders in a row

Usage:
  sh create_folders.sh
'

# Create 134 folders (number of people in AR dataset)
for i in `seq 0 134`; do mkdir $i; done
