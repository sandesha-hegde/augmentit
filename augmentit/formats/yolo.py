import os

def yolo_format(size, box):
    """

    Args:
        size: size of the image [width, height]
        box: coordinates [[xmin,ymin], [xmax, ymax]]

    Returns: Converted yolo coordinates [[x,y], [w,h]]

    """
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0][0] + box[0][1]) / 2.0
    y = (box[1][0] + box[1][1]) / 2.0

    w = box[0][1] - box[0][0]
    h = box[1][1] - box[1][0]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh

    return [[x,y], [w,h]]
