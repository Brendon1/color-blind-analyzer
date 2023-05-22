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

_M_RGB2XYZ = np.array([[0.4124564, 0.3575761, 0.1804375],
                       [0.2126729, 0.7151522, 0.0721750],
                       [0.0193339, 0.1191920, 0.9503041]])

_M_HPE = np.array([[0.4002,  0.7076, -0.0808],
                   [-0.2263, 1.1653,  0.0457],
                   [0.0,     0.0,     0.9182]])

_M_CAT16 = np.array([[0.401288, 0.650173, -0.051461],
                     [-0.250268, 1.204414, 0.045854],
                     [-0.002079, 0.048952, 0.953127]])

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