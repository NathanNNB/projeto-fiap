### Descrição do Projeto

Este projeto apresenta um aplicativo que integra as tecnologias Flask e React para oferecer funcionalidades avançadas relacionadas a dados de vinhos coletados do site da Embrapa. Por meio de endpoints que realizam scraping e análise de dados, a aplicação proporciona uma extração personalizada, flexível e eficiente de informações vitivinícolas, realizando buscas gerais ou aceitando parâmetros opcionais como ano e categoria. Sorbe a estrutura dessa API, o projeto está hospedado no Vercel para o front-end e no Render para o back-end.

### Links Úteis

Site da Embrapa: http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_01
Frontend: https://projeto-fiap-coral.vercel.app/
Backend: https://projeto-fiap.onrender.com/
Swagger: https://projeto-fiap.onrender.com/apidocs

### Estrutura do Projeto
project/ ├── backend/ │ ├── app/ │ │ └── ... │ ├── requirements.txt │ ├── run.py │ └── venv/ └── frontend/ ├── package.json ├── vite.config.js └── src/ └── ...

### Requisitos

- **Python 3.8+**  
- **Node.js 14+**  
- **npm** or **yarn**

### Diagrama e Observações

![Diagrama em branco (1)](https://github.com/user-attachments/assets/effda8a5-569b-407d-853f-3c6bd32e20f6)

#### Códigos de Status HTTP:

200 OK: Requisição bem sucedida
400 Bad Request: A requisição está incorreta em seus valores.
500 Internal Server Error: Ocorreu um erro interno no servidor, não foi possível conectar ao site da Embrapa.

### Endpoints

#### Comerce Wine Scraping (/api/comerce/) 
  - Método: GET
  - Parâmetros: ano (opcional)
  - Retorno: JSON com dados de comercialização de vinhos

#### Exports Wine Scraping (/api/exports/) 
  - Método: GET
  - Parâmetros: ano (opcional) e categoria(opcional)
  - Retorno: JSON com dados de exportação de vinhos

#### Imports Wine Scraping (/api/imports/) 
  - Método: GET
  - Parâmetros: ano (opcional) e categoria(opcional)
  - Retorno: JSON com dados de importação de vinhos

#### Processing Wine Scraping (/api/processing/) 
  - Método: GET
  - Parâmetros: ano (opcional) e categoria(opcional)
  - Retorno: JSON com dados de processamento de vinhos

#### Production Wine Scraping (/api/production/) 
  - Método: GET
  - Parâmetros: ano (opcional)
  - Retorno: JSON com dados de produção de vinhos
  
