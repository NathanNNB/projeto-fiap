# Flask + React Full Stack Project

Este projeto demonstra um aplicativo que combina Flask e React para fornecer funcionalidades relacionadas a dados de vinhos, com APIs para scraping e análise

### Resource 

http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_01

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
    source venv/bin/activate  # (Linux/Mac) or .\venv\Scripts\activate (Windows)
    
    pip install -r requirements.txt
    python run.py

Flask should be available at http://127.0.0.1:5000 (locally) or https://projeto-fiap.onrender.com/

### 2. Frontend (React)

1. Go to the `frontend` folder:  
    ```bash
    cd ../frontend
    yarn install
    yarn run dev

React should be available at http://127.0.0.1:5173 (locally) or https://projeto-fiap-coral.vercel.app/

### 3. Main Endpoints

https://projeto-fiap-coral.vercel.app/ - Frontend 

https://projeto-fiap.onrender.com/ - Backend 

### 4. Swagger

Swagger/OpenAPI Documentation

This project includes **Swagger (OpenAPI)** documentation using [Flasgger](https://github.com/flasgger/flasgger). Swagger provides an interactive UI to explore and test API endpoints.

#### How to Access
Start the Flask app (e.g., python run.py).

Open your browser and visit:
http://127.0.0.1:5000/apidocs (locally) or https://projeto-fiap.onrender.com/apidocs

-Specifc Endpoints

Comerce Wine Scraping (/api/comerce/) 
  - Método: GET
  - Parâmetros: ano (opcional)
  - Retorno: JSON com dados de comercialização de vinhos

Exports Wine Scraping (/api/exports/) 
  - Método: GET
  - Parâmetros: ano (opcional) e categoria(opcional)
  - Retorno: JSON com dados de exportação de vinhos

Imports Wine Scraping (/api/imports/) 
  - Método: GET
  - Parâmetros: ano (opcional) e categoria(opcional)
  - Retorno: JSON com dados de importação de vinhos


Processing Wine Scraping (/api/processing/) 
  - Método: GET
  - Parâmetros: ano (opcional) e categoria(opcional)
  - Retorno: JSON com dados de processamento de vinhos

Production Wine Scraping (/api/production/) 
  - Método: GET
  - Parâmetros: ano (opcional)
  - Retorno: JSON com dados de produção de vinhos
  
