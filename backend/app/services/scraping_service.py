import requests, os
from flask import jsonify
from bs4 import BeautifulSoup
from app.utils.htmlUtils import htmlToDF, create_html_file, read_defaultData

def scrape_page(url, params):
    soup = None
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  
        soup = BeautifulSoup(response.text, 'html.parser')
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a URL :{url}")
        localSoup = read_defaultData(params)
        if not localSoup:
            print(f"Not able to access content at URL {url} or in local file")
            return {f"error': 'Not able to access content at URL {url} or in local file"}
        soup = localSoup

    if not soup:
        localSoup = read_defaultData(params)

        if not localSoup:
            print(f"Not able to find HTML at {url} or in local file")
            return {f"error': 'Not able to find HTML at {url} or in local file"}
        soup = localSoup
    
    table = soup.find('table', {'class': 'tb_base tb_dados'})
    
    if not table:
        print(f"Table not found at {url}")
        return {f"error': 'Error accessing HTML {url}"}
    
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # Vai para backend/app
    target_dir = os.path.join(base_dir, "defaultData") 
    
    # Conteúdo HTML
    html_code = table
    
    # Cria o arquivo HTML no diretório defaultData
    create_html_file(target_dir, params, html_code)

    row = table.find_all('tr')
    data = htmlToDF(row)
    return data

    