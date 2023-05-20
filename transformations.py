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

def srgb_to_linear(srgb: np.ndarray):
    """
    Convert from sRGB to linear RGB.

    Removes the gamma correction of the non-linear sRGB space to
    the linear RGB space. The formula used can be found at:
    https://en.wikipedia.org/wiki/SRGB#Specification_of_the_transformation
    """

    rgb = np.float32(srgb) / 255.0
    mask = np.where(rgb > 0.04045, True, False)
    rgb[mask] = (((rgb[mask] + 0.055) / 1.055)**2.4)
    rgb[~mask] = (rgb[~mask] / 12.92)
    return rgb

def srgb_to_xyz(img: np.ndarray):
    return

def xyz_to_lms(img: np.ndarray):
    return

def srgb_to_lms(img: np.ndarray):
    srgb_to_xyz()
    xyz_to_lms()

def lms_to_srgb():
    return