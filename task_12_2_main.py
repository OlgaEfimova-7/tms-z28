from tms_21.task_12_2_classes import Circle, Triangle, Square, Point

circle = Circle(Point(0, 0), 3)
triangle = Triangle(Point(0, 0), Point(3, 0), Point(3, 3))
square = Square(Point(0, 0), Point(4, 0))
list_of_figures = [circle, triangle, square]
for i in list_of_figures:
    print(i.square())
