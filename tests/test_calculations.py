# tests/test_calculations.py
import pytest

from app.models import Cube, Sphere, Cylinder, Cone


def test_cube_volume():
    cube = Cube(3)
    assert cube.volume() == 27


def test_cube_surface_area():
    cube = Cube(3)
    assert cube.surface_area() == 54


def test_sphere_volume():
    sphere = Sphere(3)
    assert sphere.volume() == pytest.approx(113.097, 0.001)


def test_sphere_surface_area():
    sphere = Sphere(3)
    assert sphere.surface_area() == pytest.approx(113.097, 0.001)


def test_cylinder_volume():
    cylinder = Cylinder(3, 5)
    assert cylinder.volume() == pytest.approx(141.372, 0.001)


def test_cylinder_surface_area():
    cylinder = Cylinder(3, 5)
    assert cylinder.surface_area() == pytest.approx(150.796, 0.001)


def test_cone_volume():
    cone = Cone(3, 5)
    assert cone.volume() == pytest.approx(47.123, 0.001)


def test_cone_surface_area():
    cone = Cone(3, 5)
    assert cone.surface_area() == pytest.approx(83.229, 0.001)
