# YOLO Annotation Tool

## Features

The tool should help to annotate data sets with the yolo annotation style. Also it should be easy to extend it and to create pipes which should be done on the provided image. Therefore we will split the pipe into the following steps:

### Annotation

This is the most important feature. The idea is to use bounding boxes to highlight the objects in the image and after that export it.

### Preprocessing

With the annotated image we want to have several preprocessing options which care not only about the image but also about the bounding boxes.

- Scale image
- Grayscale

### Augmentation

Creating new images based on the given augmentations

- Grayscale
- Cropping
- Flipping
- Rotating

### Creation of new images

- Create a new data set and save it with the given images

## Plan of Action

- Write the code for annotation tool
