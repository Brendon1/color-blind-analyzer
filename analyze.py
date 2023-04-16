import cv2 as cv
import numpy as np
import os

# Absolute path of source directory
srcDir = os.path.join(os.getcwd(), 'source-images')
# List of all files and directories in source directory
dirList = os.listdir(srcDir)

# Print all file names in source directory
print("Files and directories in '", srcDir, "' :")
print(dirList)

# Read in all images in source directory
imgs = []
for file in dirList:
    imgs.append(cv.imread(os.path.join(srcDir, file)))

# Output all images with window name matching file name
for index, img in enumerate(imgs):
    cv.imshow(dirList[index], img)

# Maintain windows until key press
cv.waitKey(0)

# Clean up windows
cv.destroyAllWindows()
