import yolo
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches
import numpy as np
import typing
import numpy.typing
import cv2

currentLine: typing.Tuple = ()

# importing the module
import cv2

first_click = ()
img_with_line = None
current_image = None

rectangles = []


# function to display the coordinates of
# of the points clicked on the image
def click_event(event, x, y, flags, params):
    global rectangles
    global first_click
    global img_with_line
    global current_image
    # checking for left mouse clicks
    if event == cv2.EVENT_MOUSEMOVE:
        # displaying the coordinates
        # on the Shell
        img_c = current_image.copy()
        print(x, ' ', y)
        cv2.line(img_c, (x, 0), (x, img.shape[0]), (0, 255, 0))
        cv2.line(img_c, (0, y), (img.shape[1], y), (0, 255, 0))
        print(img.shape)
        cv2.imshow("image", img_c)

    if event == cv2.EVENT_LBUTTONDOWN:
        # displaying the coordinates
        # on the Shell
        img_with_line = img.copy()
        current_image = img_with_line
        print(x, ' ', y)
        cv2.line(img_with_line, (x, 0), (x, img.shape[0]), (0, 255, 0))
        cv2.line(img_with_line, (0, y), (img.shape[1], y), (0, 255, 0))
        first_click = (x, y)
        cv2.imshow("image", img_with_line)

    # checking for right mouse clicks
    if event == cv2.EVENT_RBUTTONDOWN:
        if first_click == ():
            return

        cv2.rectangle(img, first_click, (x, y), (0, 255, 0), 2)
        current_image = img
        rectangles.append((first_click, (x, y)))


# driver function
if __name__ == "__main__":
    # reading the image
    img = cv2.imread('../data/frame0_2.jpg', 1)
    current_image = img
    the_image = img

    # displaying the image
    cv2.imshow('image', img)

    # setting mouse handler for the image
    # and calling the click_event() function
    cv2.setMouseCallback('image', click_event)

    # wait for a key to be pressed to exit
    cv2.waitKey(0)

    # close the window
    cv2.destroyAllWindows()

    yolo_anno = map(lambda x: yolo.YoloAnnotation(x[0], x[1]), rectangles)
    fa = list(yolo_anno)[0]
    print(fa)

    cv2.rectangle(the_image, (fa.x, fa.y), (fa.x + fa.width, fa.y + fa.height), (0, 255, 0), 2)
    cv2.imshow("abc", the_image)
    cv2.waitKey(0)
