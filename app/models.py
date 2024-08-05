# app/models.py

from math import pi


class Shape3D:
    def volume(self):
        pass

    def surface_area(self):
        pass


class Cube(Shape3D):
    def __init__(self, side_length: float):
        self.side_length = side_length

    def volume(self):
        return self.side_length ** 3

    def surface_area(self):
        return 6 * (self.side_length ** 2)


class Sphere(Shape3D):
    def __init__(self, radius: float):
        self.radius = radius

    def volume(self):
        return (4/3) * pi * (self.radius ** 3)

    def surface_area(self):
        return 4 * pi * (self.radius ** 2)


class Cylinder(Shape3D):
    def __init__(self, radius: float, height: float):
        self.radius = radius
        self.height = height

    def volume(self):
        return pi * (self.radius ** 2) * self.height

    def surface_area(self):
        return 2 * pi * self.radius * (self.radius + self.height)


class Cone(Shape3D):
    def __init__(self, radius: float, height: float):
        self.radius = radius
        self.height = height

    def volume(self):
        return (1/3) * pi * (self.radius ** 2) * self.height

    def surface_area(self):
        slant_height = (self.radius ** 2 + self.height ** 2) ** 0.5
        return pi * self.radius * (self.radius + slant_height)

