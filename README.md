## AugmentIt
This package gives basic augmentation techniques like cropping, resizing, scaling etc, for classification, segmentation and object detection.

## Note:
This package is still in development.Now only it supports image cropping, image resizing with their annotations and yolo format conversion.

# Installation<br>

# Install
```
pip install augmentit --extra-index-url https://__token__:DEB26swtzZfvbxKyYn1E@gitlab.com/api/v4/projects/24617682/packages/pypi/simple
```
# Upgrade
```
pip install augmentit --extra-index-url https://__token__:DEB26swtzZfvbxKyYn1E@gitlab.com/api/v4/projects/24617682/packages/pypi/simple
```

# Documentation

## crop_image(image, coords, roi_coords, draw_image)

    image - Numpy image array
    coords - List of annotations [[[x1, y1], [x2,y2],..], ...]
    roi_coords - coordinates to crop the image [[x1, y1], [x2,y2],..]
    draw_image - True or False to verify the conversion

## resize_image(image, coords, roi_coords, draw_image)

    image - Numpy image array
    coords - List of annotations [[[x1, y1], [x2,y2],..], ...]
    roi_coords - coordinates to crop the image [[x1, y1], [x2,y2],..]
    draw_image - True or False to verify the conversion

## yolo_format(size, box)
    size: size of the image [width, height]
    box: coordinates [[xmin,ymin], [xmax, ymax]]

    Returns: Converted yolo coordinates [[x,y], [w,h]]

## plot_one_box(x, img, color=None, label=None, line_thickness=None)
    x: [[xmin,ymin], [xmax, ymax]]
    img: Image array

    Return: Image array

## plot_one_polygon(x, img, color=None, label=None, line_thickness=None)
    x: [[[x1,y1], [x2, y2], ..], ..]
    img: Image array

    Return: Image array
