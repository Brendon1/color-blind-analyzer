import cv2 as cv
import numpy as np

#sRGB to LMS
    #sRGB to XYZ       
       #sRGB to linear sRGB 
    #XYZ to LMS

#LMS to sRGB
    #LMS to XYZ
    #XYZ to sRGB
        #linear sRGB to sRGB
        ##RGB to BGR

def srgb_to_linear(img: np.ndarray):
    """
    Convert from sRGB to linear values.

    Removes the gamma correction of each sRGB pixel to its linear
    value. The formula used can be found at:
    https://en.wikipedia.org/wiki/SRGB#Specification_of_the_transformation
    """

    # TODO: verify with testing
    img = img / 255.0
    img = ((img / 12.92) if (img <= 0.04045) else (((img + 0.055) / 1.055)**2.4))

def srgb_to_xyz(img: np.ndarray):
    return

def xyz_to_lms(img: np.ndarray):
    return

def srgb_to_lms(img: np.ndarray):
    srgb_to_xyz()
    xyz_to_lms()

def lms_to_srgb():
    return