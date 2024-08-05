# tests/test_endpoints.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_cube_volume_endpoint():
    response = client.post("/cube/volume", json={"side_length": 3})
    assert response.status_code == 200
    assert response.json() == {"volume": 27}


def test_cube_surface_area_endpoint():
    response = client.post("/cube/surface_area", json={"side_length": 3})
    assert response.status_code == 200
    assert response.json() == {"surface_area": 54}


def test_sphere_volume_endpoint():
    response = client.post("/sphere/volume", json={"radius": 3})
    assert response.status_code == 200
    assert response.json() == {"volume": pytest.approx(113.097, 0.001)}


def test_sphere_surface_area_endpoint():
    response = client.post("/sphere/surface_area", json={"radius": 3})
    assert response.status_code == 200
    assert response.json() == {"surface_area": pytest.approx(113.097, 0.001)}


def test_cylinder_volume_endpoint():
    response = client.post("/cylinder/volume", json={"radius": 3, "height": 5})
    assert response.status_code == 200
    assert response.json() == {"volume": pytest.approx(141.372, 0.001)}


def test_cylinder_surface_area_endpoint():
    response = client.post("/cylinder/surface_area", json={"radius": 3, "height": 5})
    assert response.status_code == 200
    assert response.json() == {"surface_area": pytest.approx(150.796, 0.001)}


def test_cone_volume_endpoint():
    response = client.post("/cone/volume", json={"radius": 3, "height": 5})
    assert response.status_code == 200
    assert response.json() == {"volume": pytest.approx(47.123, 0.001)}


def test_cone_surface_area_endpoint():
    response = client.post("/cone/surface_area", json={"radius": 3, "height": 5})
    assert response.status_code == 200
    assert response.json() == {"surface_area": pytest.approx(83.229, 0.001)}
