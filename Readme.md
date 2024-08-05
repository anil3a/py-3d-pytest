# 3D Shapes Calculator with FastAPI

This project is a FastAPI application that performs complex calculations on 3D shapes such as Cube, Sphere, Cylinder, and Cone. It provides RESTful API endpoints to calculate the volume and surface area of these shapes. The application also includes unit tests using `pytest`.

## Features

- Calculate volume and surface area for Cube, Sphere, Cylinder, and Cone.
- RESTful API endpoints built with FastAPI.
- Unit tests with pytest.
- Dockerized for easy deployment.
- Continuous deployment with GitHub Actions ~~(example with Heroku)~~.

## Installation

### Prerequisites

- Python 3.11 or higher
- Pip
- Git

### Setting Up the Environment

1. Clone the repository:

    ```bash
    git clone https://github.com/anil3a/py-3d-pytest.git
    cd 3d_shapes_calculator
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. Start the FastAPI server:

    ```bash
    uvicorn app.main:app --reload
    ```

2. Open your browser and navigate to `http://127.0.0.1:8500/docs` to access the interactive API documentation.

## API Endpoints

- `POST /cube/volume`: Calculate the volume of a cube.
- `POST /cube/surface_area`: Calculate the surface area of a cube.
- `POST /sphere/volume`: Calculate the volume of a sphere.
- `POST /sphere/surface_area`: Calculate the surface area of a sphere.
- `POST /cylinder/volume`: Calculate the volume of a cylinder.
- `POST /cylinder/surface_area`: Calculate the surface area of a cylinder.
- `POST /cone/volume`: Calculate the volume of a cone.
- `POST /cone/surface_area`: Calculate the surface area of a cone.

## Testing

Run the tests with `pytest`:

```bash
pytest tests
```


## Docker Deployment
1. Build the Docker image:

   ```bash
     docker build -t 3d_shapes_calculator .
   ```

2. Run the Docker container:
   
   ```bash
   docker run -p 8000:8000 3d_shapes_calculator
   ```

## Contributing
1. Fork the repository.
2. Create a new branch (git checkout -b feature/your-feature).
3. Make your changes.
4. Commit your changes (git commit -am 'Add some feature').
5. Push to the branch (git push origin feature/your-feature).
6. Create a new Pull Request.


## License
This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgements
- FastAPI
- Pytest

### Conclusion
This `README.md` provides a comprehensive overview of your project, including installation instructions, API endpoints, testing, deployment, and contribution guidelines. Feel free to customize it further based on your specific project details and preferences.
