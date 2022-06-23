import typing


class YoloAnnotation:
    object_class: int
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
        return f"x: {self.x}, y: {self.y}, width: {self.width}, height: {self.height}"
