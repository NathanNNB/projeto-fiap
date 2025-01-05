import requests
from bs4 import BeautifulSoup

def scrape_page(url):
    response = requests.get(url)
    response.raise_for_status()  # levanta erro se status_code != 200

    soup = BeautifulSoup(response.text, 'html.parser')
    # Exemplo: extrair todos os <h2>
    h2_tags = [h2.get_text(strip=True) for h2 in soup.find_all('h2')]
    return h2_tags