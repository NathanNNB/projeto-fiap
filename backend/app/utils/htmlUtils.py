import os
import pandas as pd
from bs4 import BeautifulSoup

def htmlToDF(htmlTable):
    if htmlTable is None:
        return None

    data = []

    # 'htmlTable' is a list (ResultSet) of <tr> elements.
    for row in htmlTable:
        # Now call .find_all() on this row (which is a single <tr>).
        cells = row.find_all(['th', 'td'])

        cells_text = [cell.get_text(strip=True) for cell in cells]
        data.append(cells_text)

    df = pd.DataFrame(data[1:], columns=data[0]) if len(data) > 1 else pd.DataFrame(data)
    data_as_list = df.to_dict(orient="records")
    return data_as_list

def create_html_file(directory, filename, html_content):

    filename = f"{filename}.html"
    # 1. Ensure the directory exists (create it if not)
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory created: {directory}")
    else:
        print(f"Directory already exists: {directory}")
    
    # 2. Construct the full path for the file
    file_path = os.path.join(directory, filename)
    
    # 3. Write the HTML content to the file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(html_content))
    
    print(f"HTML file created at: {file_path}")

def read_defaultData(fileName):

    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # Vai para backend/app
    target_dir = os.path.join(base_dir, "defaultData") 
    file_path = f"{target_dir}/{fileName}"
    try:
        # 1. Abrir o arquivo e ler o conteúdo
        file_path += ".html" 
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        
        # 2. Parsear o HTML com BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        return soup
    
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"Error reading the file: {e}")
        return None
    
def transformDf(htmlTable):
    if htmlTable is None:
        return None

    data = []
    current_category = None  # Para rastrear o item atual

    # 'htmlTable' é uma lista (ResultSet) de elementos <tr>.
    for row in htmlTable:
        # Encontrar todas as células da linha (th ou td)
        cells = row.find_all(['th', 'td'])
        cells_text = [cell.get_text(strip=True) for cell in cells]
        cell_classes = [cell.get("class", []) for cell in cells][0]
        print(cell_classes)
        # Verificar se a linha é um "item" ou "subitem"
        if "tb_item" in cell_classes:  # Substitua "item-class" pela classe ou lógica que define o item
            current_category = cells_text[0]  # Defina o nome do item como a primeira célula (ajuste conforme necessário)
        elif "tb_subitem" in cell_classes:  # Substitua "subitem-class" pela lógica para subitens
            if current_category:  # Só adiciona se já houver um item atual
                data.append([current_category] + cells_text)
    # Criar DataFrame com a primeira coluna sendo 'Categoria'
    print(len(data[0]))
    df = pd.DataFrame(data, columns= [f"Coluna_{i}" for i in range(0, len(data[0]))]) if data else pd.DataFrame()
    data_as_list = df.to_dict(orient="records")
    return data_as_list