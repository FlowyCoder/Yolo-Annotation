import typing
import os
import pathlib


class YoloAnnotation:
    object_class: int = 0
    x: int
    y: int
    width: int
    height: int

    def __init__(self, point1: typing.Tuple[int, int], point2: typing.Tuple[int, int]):
        point1_x = point1[0]
        point2_x = point2[0]
        if point1_x > point2_x:
            self.x = point2_x
            self.width = point1_x - point2_x
        else:
            self.x = point1_x
            self.width = point2_x - point1_x
        point1_y = point1[1]
        point2_y = point2[1]
        if point1_y > point2_y:
            self.y = point2_y
            self.height = point1_y - point2_y
        else:
            self.y = point1_y
            self.height = point2_y - point1_y

    def __str__(self):
        return f"class: {self.object_class}, x: {self.x}, y: {self.y}, width: {self.width}, height: {self.height}"

    def export(self):
        return f"{self.object_class} {self.x} {self.y} {self.width} {self.height}"


class ImageAnnotation:
    imageName: str  # Without ending
    annotations: typing.List[YoloAnnotation]

    def __init__(self, image_name_: str, annotations_: typing.List[YoloAnnotation]):
        self.imageName = image_name_
        self.annotations = annotations_

    def saveAnnotation(self):
        # Write annotations in the file
        path = pathlib.Path(f'../labels/{self.imageName}.txt')
        if path.exists():
            os.remove(path.absolute())

        opened_path = path.open('w')
        anno_str = [x.export() for x in self.annotations]
        opened_path.writelines(anno_str)
