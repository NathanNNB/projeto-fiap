from flask import Blueprint, jsonify, request
from flasgger import swag_from
from app.routes.routes import URL
from app.services.scraping_service import scrape_page

IMPORTS_PARAM = 'opcao=opt_05' 

imports = Blueprint('imports', __name__)

@imports.route('/api/imports/', methods=['GET'])
@swag_from({
    'tags': ['Imports Wine Scraping'],
    'description': 'Endpoint que realiza web scraping em uma página de importação de vinhos, retornando informações sobre vinhos de um ano especificado.',
    'parameters': [
        {
            'name': 'year',
            'in': 'query',
            'description': 'Ano dos vinhos a serem buscados.',
            'required': False,
            'schema': {
                'type': 'integer',
                'example': 2020
            }
        },
                {
            'name': 'classification',
            'in': 'query',
            'description': 'Classificação a ser buscada',
            'required': False,
            'schema': {
                'type': 'string',
                'enum': ['subopt_01', 'subopt_02', 'subopt_03', 'subopt_04', 'subopt_05' ],
                'example': 'subopt_02'
            }
        },
    ],
    'responses': {
        200: {
            'description': 'Sucesso - Informações sobre os vinhos retornadas.',
            'content': {
                'application/json': {
"message": "[{'Países': 'Africa do Sul', 'Quantidade (Kg)': '3.574', 'Valor (US$)': '14.542'}, {'Países': 'Alemanha', 'Quantidade (Kg)': '21.174', 'Valor (US$)': '65.359'}, {'Países': 'Argentina', 'Quantidade (Kg)': '469.547', 'Valor (US$)': '1.304.986'}, {'Países': 'Austrália', 'Quantidade (Kg)': '7.426', 'Valor (US$)': '15.190'}, {'Países': 'Áustria', 'Quantidade (Kg)': '909', 'Valor (US$)': '9.399'}, {'Países': 'Bermudas', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Bahamas', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Bélgica', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Brasil', 'Quantidade (Kg)': '3.491', 'Valor (US$)': '106.310'}, {'Países': 'Bulgária', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Canada', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Chile', 'Quantidade (Kg)': '253.225', 'Valor (US$)': '775.535'}, {'Países': 'Croácia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Cuba', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Emirados Árabes Unidos', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Eslovênia', 'Quantidade (Kg)': '68', 'Valor (US$)': '327'}, {'Países': 'Espanha', 'Quantidade (Kg)': '1.421.655', 'Valor (US$)': '3.871.128'}, {'Países': 'Estados Unidos', 'Quantidade (Kg)': '13.255', 'Valor (US$)': '31.083'}, {'Países': 'França', 'Quantidade (Kg)': '1.116.188', 'Valor (US$)': '8.814.571'}, {'Países': 'Geórgia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Granada', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Grécia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Hong Kong', 'Quantidade (Kg)': '72', 'Valor (US$)': '5.061'}, {'Países': 'Hungria', 'Quantidade (Kg)': '765', 'Valor (US$)': '2.061'}, {'Países': 'Indonésia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Irlanda', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Israel', 'Quantidade (Kg)': '296', 'Valor (US$)': '9.540'}, {'Países': 'Itália', 'Quantidade (Kg)': '1.524.542', 'Valor (US$)': '3.544.718'}, {'Países': 'Luxemburgo', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'México', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Moldávia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Nova Zelândia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Países Baixos', 'Quantidade (Kg)': '3.412', 'Valor (US$)': '151.690'}, {'Países': 'Panamá', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Peru', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Portugal', 'Quantidade (Kg)': '102.324', 'Valor (US$)': '324.099'}, {'Países': 'Reino Unido', 'Quantidade (Kg)': '2.309', 'Valor (US$)': '17.975'}, {'Países': 'Romênia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Suíça', 'Quantidade (Kg)': '481', 'Valor (US$)': '15.222'}, {'Países': 'Tunísia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Ucrânia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Uruguai', 'Quantidade (Kg)': '2.908', 'Valor (US$)': '18.124'}, {'Países': 'Não consta na tabela', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Não declarados', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Outros', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Total', 'Quantidade (Kg)': '4.947.621', 'Valor (US$)': '19.096.920'}]"          }
            }
        },
        400: {
            'description': 'Requisição inválida - Ano informado fora do período aceitado',
            'content': {
                'application/json': {
                    'example': {
                        "message": "{Invalid Year, use a value between 1970 and 2023}"
                    }
                }
            }
        },
        500: {
            'description': 'Erro interno no servidor - Falha durante o processo de web scraping.',
            'content': {
                'application/json': {
                    'example': {
                        'error': 'Erro ao realizar scraping. Por favor, tente novamente mais tarde.'
                    }
                }
            }
        }
    }
})
def getImports():
    importsURL = URL
    params = IMPORTS_PARAM

    year = request.args.get('year', default='', type=str)
    classification = request.args.get('classification', default='', type=str)

    if year:
        if not 1970 <= int(year) <= 2023:
            return jsonify({"message": "{Invalid Year, use a value between 1970 and 2023}"})
        yearParameter = f"ano={year}&"
        importsURL = f"{importsURL}{yearParameter}"
        params = f"{params}{year}"

    if classification: 
        classificationParameter = f"subopcao={classification}&"
        importsURL= f"{importsURL}{classificationParameter}"
        params = f"{params}{classification}"

    importsURL = f"{importsURL}{IMPORTS_PARAM}" 
    data = scrape_page(importsURL, params)
    if "error" in data:
        return data
    return jsonify({"message": str(data)})


