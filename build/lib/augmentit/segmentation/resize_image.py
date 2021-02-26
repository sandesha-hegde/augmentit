import numpy as np
import cv2
from augmentit.draw.plot_box import plot_one_box, plot_one_polygon
import copy


def resize_image(image, coords, new_shape, draw_img=True):
    '''

    Args:
        image: Numpy image array
        coords: list of coordinates can be bbox or polygon, [[[xmin, ymin], [xmax, ymax]], ....]
        new_shape: Resize shape[height, width]
        draw_img: coordinates need to drawn on image True or False

    Returns: dictionary which has resized image, resized coordinates, and draw image.

    '''

    h, w = image.shape[:2]
    scale_x = new_shape[1] / w
    scale_y = new_shape[0] / h

    rimage = cv2.resize(image, (new_shape[1], new_shape[0]))
    orig_img = copy.deepcopy(rimage)

    new_coords = []

    for coord in coords:
        temp_coords = []
        for c in coord:
            x = int(np.round(c[0] * scale_x))
            y = int(np.round(c[1] * scale_y))

            temp_coords.append([x, y])

        if draw_img:

            if len(temp_coords) == 2:
                plot_one_box(temp_coords, rimage)
            if len(temp_coords) > 2:
                plot_one_polygon(temp_coords, rimage)

        new_coords.append(temp_coords)

    result_dict = {'resized image': orig_img, 'drawn image': rimage, 'resized coords': new_coords}

    return result_dict
