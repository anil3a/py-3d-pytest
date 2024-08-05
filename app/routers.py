# app/routers.py

from fastapi import APIRouter
from pydantic import BaseModel
from .models import Cube, Sphere, Cylinder, Cone

router = APIRouter()


class CubeModel(BaseModel):
    side_length: float


class SphereModel(BaseModel):
    radius: float


class CylinderModel(BaseModel):
    radius: float
    height: float


class ConeModel(BaseModel):
    radius: float
    height: float


@router.post("/cube/volume")
def calculate_cube_volume(cube: CubeModel):
    shape = Cube(cube.side_length)
    return {"volume": shape.volume()}


@router.post("/cube/surface_area")
def calculate_cube_surface_area(cube: CubeModel):
    shape = Cube(cube.side_length)
    return {"surface_area": shape.surface_area()}


@router.post("/sphere/volume")
def calculate_sphere_volume(sphere: SphereModel):
    shape = Sphere(sphere.radius)
    return {"volume": shape.volume()}


@router.post("/sphere/surface_area")
def calculate_sphere_surface_area(sphere: SphereModel):
    shape = Sphere(sphere.radius)
    return {"surface_area": shape.surface_area()}


@router.post("/cylinder/volume")
def calculate_cylinder_volume(cylinder: CylinderModel):
    shape = Cylinder(cylinder.radius, cylinder.height)
    return {"volume": shape.volume()}


@router.post("/cylinder/surface_area")
def calculate_cylinder_surface_area(cylinder: CylinderModel):
    shape = Cylinder(cylinder.radius, cylinder.height)
    return {"surface_area": shape.surface_area()}


@router.post("/cone/volume")
def calculate_cone_volume(cone: ConeModel):
    shape = Cone(cone.radius, cone.height)
    return {"volume": shape.volume()}


@router.post("/cone/surface_area")
def calculate_cone_surface_area(cone: ConeModel):
    shape = Cone(cone.radius, cone.height)
    return {"surface_area": shape.surface_area()}
