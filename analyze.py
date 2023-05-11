import cv2 as cv
import numpy as np
import os
import sys
import argparse

def restrict_float_input(x):
    try:
        x = float(x)
    except ValueError:
        raise argparse.ArgumentTypeError("%r is not a floating-point" % x)
    
    if x <= 0.0 or x > 1.0:
        raise argparse.ArgumentTypeError("%r is not in range (0.0, 1.0]" % x)
    return x

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--classification', type=str.lower,
                        choices=['protanopia', 'deuteranopia', 'tritanopia', 'achromatopsia'],
                        required=True, metavar='', help='Classification of colorblindness to analyze')
    parser.add_argument('-i', '--intensity', type=float, default=1.0, choices=restrict_float_input,
                        metavar='', help='The intensity of the colorblindness classification')
    parser.add_argument('-s', '--source', type=str, default=os.path.join(os.getcwd(), 'source'),
                        metavar='', help='Path of directory containing files to analyze')
    parser.add_argument('-d', '--destination', type=str, default=os.path.join(os.getcwd(), 'destination'),
                        metavar='', help='Path of directory to save analyzed files')
    parser.add_argument('-f', '--file-type', type=str, default='.png', metavar='', help='File type to \
                        analyze')
    parser.add_argument('-sz', '--region-size', type=int, default=20, metavar='', help='The size of each \
                        region to be analyzed. [Smaller-size]: greater resolution, susceptible to noise. \
                        [Larger-size]: more efficient, loses granularity')
    parser.add_argument('-t', '--threshold', type=int, metavar='', help='Threshold for if a region is \
                        problematic')
    return parser.parse_args()

def main():
    args = get_args()

    # Absolute path of source directory
    srcDir = os.path.join(os.getcwd(), 'source')
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

    detect_edges()

if __name__ == '__main__':
    main()

def detect_edges():
    print("CALL_TO: dect_edges\n")

def num_edge_pixels():
    print("CALL_TO: num_edge_pixels\n")

def avg_edge_strength():
    print("CALL_TO: avg_edge_strength\n")

def edge_difference():
    """
    Calculate how different the edges of two images are in a region.

    The method for calculating the difference in edges is acheived by
    a summing the differences between the number of detected edges
    and average edge strength in the two regions.
    """

    print("CALL_TO: edge_difference\n")
    orig_edge_count = 0
    cb_edge_count = 0
    orig_avg_edge_strength = 0
    cb_avg_edge_strength = 0

    # TODO: may want to filter out cases where colorblindness 
    # creates a greater contrast than the original
    return abs(orig_edge_count - cb_edge_count) + abs(orig_avg_edge_strength - cb_avg_edge_strength)

def analyze_region():
    """
    Determine if a region of pixels is problematic.

    A region is concidered problematic if the difference in the
    edges is greater than some threshold. The threshold value can
    be decreased or increased to make the analysis respectively 
    more or less sensetive to the differences. 
    """

    print("CALL_TO: analyze_region\n")
    threshold = 0

    if edge_difference() > threshold:
        print("Problematic area found")

