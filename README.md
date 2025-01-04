# Flask + React Full Stack Project

A simple full-stack application featuring a **Flask** backend and a **React** frontend.

## Project Structure
project/ ├── backend/ │ ├── app/ │ │ └── ... │ ├── requirements.txt │ ├── run.py │ └── venv/ └── frontend/ ├── package.json ├── vite.config.js └── src/ └── ...

## Requirements

- **Python 3.8+**  
- **Node.js 14+**  
- **npm** or **yarn**

## Getting Started

### 1. Backend (Flask)

1. Go to the `backend` folder:
    ```bash
    cd backend
    python -m venv venv
    source venv/bin/activate  # (Linux/Mac)
# or venv\Scripts\activate (Windows)
    pip install -r requirements.txt
    python run.py
Flask should be available at http://127.0.0.1:5000.

### 2. Frontend (React)

1. Go to the `frontend` folder:  
    cd ../frontend
    yarn install
    yarn run dev

React should be available at http://127.0.0.1:5173.

Usage
Access http://127.0.0.1:5173 for the React app.
It communicates with the Flask API at http://127.0.0.1:5000.

### 3. Endpoints

The Flask API exposes the following endpoints by default (examples):

GET /api/hello
POST /api/data