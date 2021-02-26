import cv2
import copy
import numpy as np
import numpy
from augmentit.draw.plot_box import plot_one_box, plot_one_polygon

def crop_image(image, coords, roi_coords, draw_img = True):
    """This method is to resize the given image by cropping the image to certain size and resize the coordinates accordingly  

    Args:
        image ([Numpy array]): Image 
        coords ([list[list]]): coordinates [[[xmin, ymin],[xmax, ymax]],...]
        roi_coords ([list]): crop coordinates [[xmin, ymin],[xmax, ymax]]
        draw_img (bool, optional): [description]. Defaults to True.

    Returns:
        [type]: [description]
    """
    
    assert (image is not None), "Image is Empty"

    assert coords != [], "Coordinates are Empty"
    assert type(coords[0][0]) == list, "Coordinates format should be [[[xmin,ymin],[xmax, ymax]],...]"

    assert roi_coords != [], "Roi coordinates are Empty"


    if not isinstance(image, numpy.ndarray):
        image = numpy.array(image)

        print("Warning: Please use numpy array format....................")


    # if len(roi_coords) > 2 and type(roi_coords[0]) == list:
    rect = cv2.boundingRect(np.int32(roi_coords))
        
    roi_coords = [rect[0], rect[1], rect[0] + rect[2], rect[1] + rect[3]]


    cropped = image[roi_coords[1]: roi_coords[3], roi_coords[0]: roi_coords[2]]

    nh, nw = cropped.shape[:2]

    orig_img = copy.deepcopy(cropped)
    cxmin = roi_coords[0]
    cymin = roi_coords[1]

    new_coords = []

    for coord in coords:
        # coord = [[coord[0], coord[1]], [coord[2], coord[3]]]
        temp_coords = []
        for c in coord:
            x = int(c[0]) - int(cxmin)
            y = int(c[1]) - int(cymin)

            if x <= 0:
                x = 0
            if y <= 0:
                y = 0
                
            if x > int(roi_coords[2]):
                x = nh
            if y > int(roi_coords[3]):
                y = nw
                
            temp_coords.append([x,y])

        if draw_img:

            if len(temp_coords) == 2:
                cropped = plot_one_box(temp_coords, cropped)
            if len(temp_coords) > 2:
                cropped = plot_one_polygon(temp_coords, cropped)

            # assert len(temp_coords) > 2, "Coordinates atleast should have 4 points"



        new_coords.append(temp_coords)


    result_dict = {'resized image': orig_img, 'drawn image': cropped, 'resized coords': new_coords}
        

    
    return result_dict





        
