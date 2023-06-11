import cv2 as cv
import numpy as np

_M_RGB2XYZ = np.array([[0.4124564, 0.3575761, 0.1804375],
                       [0.2126729, 0.7151522, 0.0721750],
                       [0.0193339, 0.1191920, 0.9503041]])

_M_XYZ2RGB = np.array([[3.2404542,-1.5371385,-0.4985314],
                       [-0.9692660,1.8760108, 0.0415560],
                       [0.0556434,-0.2040259, 1.0572252]])

_M_RGB2LMS_HPE = np.array([[0.31399022, 0.63951294, 0.04649755],
                           [0.15537241, 0.75789446, 0.08670142],
                           [0.01775239, 0.10944209, 0.87256922]])

_M_LMS2RGB_HPE = np.array([[5.47221205,-4.64196011, 0.16963706],
                           [-1.12524192,2.29317097,-0.16789520],
                           [0.02980163,-0.19318070, 1.16364790]])

_M_HPE = np.array([[0.4002,  0.7076, -0.0808],
                   [-0.2263, 1.1653,  0.0457],
                   [0.0,     0.0,     0.9182]])

_M_HPE_INV = np.array([[1.86006661,-1.12948008, 0.21989830],
                       [0.36122292, 0.63880431,-0.00000713],
                       [0.0,        0.0,        1.08908734]])

_M_CAT16 = np.array([[0.401288, 0.650173, -0.051461],
                     [-0.250268, 1.204414, 0.045854],
                     [-0.002079, 0.048952, 0.953127]])

def srgb_to_linear(srgb: np.ndarray):
    """
    Convert from sRGB to linear sRGB color space.

    Removes the gamma correction of the non-linear sRGB space to
    obtain the linear sRGB space. The formula used can be found at:
    https://en.wikipedia.org/wiki/SRGB#Specification_of_the_transformation
    """

    rgb = np.float32(srgb) / 255.0
    mask = np.where(rgb > 0.04045, True, False)
    rgb[mask] = (((rgb[mask] + 0.055) / 1.055)**2.4)
    rgb[~mask] = (rgb[~mask] / 12.92)
    return rgb

def linear_to_srgb(rgb: np.ndarray):
    """
    Convert from linear sRGB to non-linear sRGB color space.

    Restores the gamma correction to the linear sRGB space to
    obtain the non-linear sRGB space. The formula used can be
    found at:
    http://www.brucelindbloom.com/index.html?Eqn_RGB_XYZ_Matrix.html
    """

    mask = np.where(rgb > 0.0031308, True, False)
    srgb[mask] = ((1.055 * srgb[mask] **(1.0/2.4)) - 0.055)
    srgb[~mask] = (srgb[~mask] * 12.92)
    srgb = np.float32(srgb) * 255.0
    return srgb

def srgb_to_xyz(srgb: np.ndarray):
    """
    Convert from sRGB to XYZ color space.

    Takes in an array using non-linear sRGB color space and converts 
    it to the linear XYZ color space by first linearizing the sRGB 
    source then applying a transformation matrix _M_RGB2XYZ. 
    The formula for the conversion can be found at:
    http://www.brucelindbloom.com/index.html?Eqn_RGB_to_XYZ.html
    and the transformation matrix used at:
    http://www.brucelindbloom.com/index.html?Eqn_RGB_XYZ_Matrix.html
    """

    rgb = srgb_to_linear(srgb)
    xyz = cv.transform(rgb, _M_RGB2XYZ)
    return xyz

def xyz_to_srgb(xyz: np.ndarray):
    """
    Convert from XYZ to sRGB color space.

    Takes in an array using using the XYZ color space and converts
    it to the non-linear sRGB color space by first applying a
    transformation matrix _M_XYZ2RGB then restores the gamma
    correction to obtain the non-linear sRGB representation.
    The formula for the conversion can be found at:
    http://www.brucelindbloom.com/index.html?Eqn_RGB_XYZ_Matrix.html
    and the transformation matrix used at:
    http://www.brucelindbloom.com/index.html?Eqn_RGB_XYZ_Matrix.html
    """

    rgb = cv.transform(xyz, _M_XYZ2RGB)
    srgb = linear_to_srgb(rgb)
    return srgb

def xyz_to_lms(xyz: np.ndarray):
    """
    Convert from XYZ to LMS color space.

    Uses the Hunt-Pointer-Estevez transformation matrix(HPE) to
    convert from XYZ to the LMS color space. The transformation
    used can be found at:
    https://en.wikipedia.org/wiki/LMS_color_space
    There is currently no difinitive best tranformation matrix
    for converting between XYZ and LMS. Other matricies such as
    CAT16, Bradford, etc. are other alternatives but this implementation
    uses HPE.
    """

    lms = cv.transform(xyz, _M_HPE)
    return lms

def lms_to_xyz(lms: np.ndarray):
    """
    Convert from LMS to XYZ color space.

    Uses the inverse Hunt-Pointer-Estevez transformation matrix
    to convert from LMS to the XYZ color space. The original
    transformation matrix can be found at:
    https://en.wikipedia.org/wiki/LMS_color_space
    There is currently no difinitive best tranformation matrix
    for converting between XYZ and LMS. Other matricies such as
    CAT16, Bradford, etc. are other alternatives but this implementation
    uses HPE.
    """

    xyz = cv.transform(lms, _M_HPE_INV)
    return xyz

def srgb_to_lms(srgb: np.ndarray):
    """
    Convert from sRGB to LMS color space.

    Uses a direct mapping to convert from sRGB to LMS by first
    linearizing the source srgb then using the transformation matrix
    _M_RGB2LMS_HPE = HPE * RGB2XYZ.
    """

    rgb = srgb_to_linear(srgb)
    lms = cv.transform(rgb, _M_RGB2LMS_HPE)
    return lms

def lms_to_srgb(lms: np.ndarray):
    """
    Convert from LMS to sRGB color space.

    Uses a direct mapping to convert from LMS to sRGB by first
    using the transformation matrix _M_LMS2RGB_HPE = inv(_M_RGB2LMS_HPE)
    then restoring the gamma correction to obtain the non-linear
    sRGB representation.
    """

    rgb = cv.transform(lms, _M_LMS2RGB_HPE)
    srgb = linear_to_srgb(rgb)
    return srgb