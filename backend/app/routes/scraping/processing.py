from flask import Blueprint, jsonify, request
from flasgger import swag_from
from app.routes.routes import URL
from app.services.scraping_service import scrape_page

PROCESSING_PARAM = 'opcao=opt_06' 

processing = Blueprint('processing', __name__)

@processing.route('/api/processing/', methods=['GET'])
@swag_from({
    'tags': ['Processing Wine Scraping'],
    'description': 'Endpoint que realiza web scraping em uma página de processamento de vinhos, retornando informações sobre vinhos de um ano especificado.',
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
                'enum': ['subopt_01', 'subopt_02', 'subopt_03', 'subopt_04'],
                'example': 'subopt_02'
            }
        },
    ],
    'responses': {
        200: {
            'description': 'Sucesso - Informações sobre os vinhos retornadas.',
            'content': {
                'application/json': {
                    "message": "[{'Países': 'África do Sul', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Alemanha', 'Quantidade (Kg)': '1.164', 'Valor (US$)': '6.560'}, {'Países': 'Angola', 'Quantidade (Kg)': '26.383', 'Valor (US$)': '141.588'}, {'Países': 'Antigua e Barbuda', 'Quantidade (Kg)': '65', 'Valor (US$)': '146'}, {'Países': 'Antilhas Holandesas', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Argentina', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Aruba', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Australia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Bahamas', 'Quantidade (Kg)': '56', 'Valor (US$)': '194'}, {'Países': 'Bangladesh', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Barbados', 'Quantidade (Kg)': '25', 'Valor (US$)': '101'}, {'Países': 'Belgica', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Benin', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Bermudas', 'Quantidade (Kg)': '12', 'Valor (US$)': '58'}, {'Países': 'Bolívia', 'Quantidade (Kg)': '22.307', 'Valor (US$)': '70.416'}, {'Países': 'Bósnia-Herzegovina', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Bulgaria', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Cabo Verde', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Camarões', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Canada', 'Quantidade (Kg)': '62', 'Valor (US$)': '347'}, {'Países': 'Catar', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Cayman, Ilhas', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Chile', 'Quantidade (Kg)': '4', 'Valor (US$)': '19'}, {'Países': 'China', 'Quantidade (Kg)': '8.619', 'Valor (US$)': '35.079'}, {'Países': 'Chipre', 'Quantidade (Kg)': '382', 'Valor (US$)': '931'}, {'Países': 'Cingapura', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Colombia', 'Quantidade (Kg)': '15.396', 'Valor (US$)': '56.227'}, {'Países': 'Coreia do Sul, Republica da', 'Quantidade (Kg)': '10', 'Valor (US$)': '30'}, {'Países': 'Costa Rica', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Cuba', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Curaçao', 'Quantidade (Kg)': '3.487', 'Valor (US$)': '15.494'}, {'Países': 'Dinamarca', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Dominica', 'Quantidade (Kg)': '594', 'Valor (US$)': '1.461'}, {'Países': 'El Salvador', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Emirados Arabes Unidos', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Equador', 'Quantidade (Kg)': '135', 'Valor (US$)': '500'}, {'Países': 'Espanha', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Estados Unidos', 'Quantidade (Kg)': '732.209', 'Valor (US$)': '1.964.451'}, {'Países': 'Estonia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Falkland (Malvinas)', 'Quantidade (Kg)': '360', 'Valor (US$)': '2.081'}, {'Países': 'Filipinas', 'Quantidade (Kg)': '77', 'Valor (US$)': '389'}, {'Países': 'Filânldia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'França', 'Quantidade (Kg)': '772', 'Valor (US$)': '4.308'}, {'Países': 'Gana', 'Quantidade (Kg)': '12.729', 'Valor (US$)': '58.137'}, {'Países': 'Gibraltar', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Granada', 'Quantidade (Kg)': '1.122', 'Valor (US$)': '3.050'}, {'Países': 'Grécia', 'Quantidade (Kg)': '38', 'Valor (US$)': '177'}, {'Países': 'Guatemala', 'Quantidade (Kg)': '284', 'Valor (US$)': '1.527'}, {'Países': 'Guiana', 'Quantidade (Kg)': '5.553', 'Valor (US$)': '26.216'}, {'Países': 'Guiné Equatorial', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Guiné-Bissau', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Haiti', 'Quantidade (Kg)': '4.842', 'Valor (US$)': '9.417'}, {'Países': 'Honduras', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Hong Kong', 'Quantidade (Kg)': '1.175', 'Valor (US$)': '5.328'}, {'Países': 'Hungria', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Ilha de Man', 'Quantidade (Kg)': '2', 'Valor (US$)': '20'}, {'Países': 'Índia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Iraque', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Irlanda', 'Quantidade (Kg)': '6', 'Valor (US$)': '22'}, {'Países': 'Islândia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Itália', 'Quantidade (Kg)': '503', 'Valor (US$)': '3.702'}, {'Países': 'Japão', 'Quantidade (Kg)': '2.970', 'Valor (US$)': '12.049'}, {'Países': 'Jordânia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Letônia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Líbano', 'Quantidade (Kg)': '1.350', 'Valor (US$)': '4.810'}, {'Países': 'Libéria', 'Quantidade (Kg)': '1.105', 'Valor (US$)': '3.367'}, {'Países': 'Luxemburgo', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Maldivas', 'Quantidade (Kg)': '3.221', 'Valor (US$)': '10.680'}, {'Países': 'Malta', 'Quantidade (Kg)': '191', 'Valor (US$)': '822'}, {'Países': 'Marshall, Ilhas', 'Quantidade (Kg)': '1.154', 'Valor (US$)': '3.438'}, {'Países': 'Montenegro', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'México', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Nicarágua', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Nigéria', 'Quantidade (Kg)': '6.705', 'Valor (US$)': '32.586'}, {'Países': 'Noruega', 'Quantidade (Kg)': '483', 'Valor (US$)': '9.852'}, {'Países': 'Nova Zelândia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Países Baixos (Holanda)', 'Quantidade (Kg)': '707', 'Valor (US$)': '6.038'}, {'Países': 'Panamá', 'Quantidade (Kg)': '3.092', 'Valor (US$)': '32.540'}, {'Países': 'Paraguai', 'Quantidade (Kg)': '48.160', 'Valor (US$)': '183.187'}, {'Países': 'Peru', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Polônia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Porto Rico', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Portugal', 'Quantidade (Kg)': '56', 'Valor (US$)': '612'}, {'Países': 'Quênia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Reino Unido', 'Quantidade (Kg)': '9.305', 'Valor (US$)': '53.968'}, {'Países': 'Republica Dominicana', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Republica Tcheca', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Rússia', 'Quantidade (Kg)': '990', 'Valor (US$)': '5.280'}, {'Países': 'Serra Leoa', 'Quantidade (Kg)': '225', 'Valor (US$)': '1.165'}, {'Países': 'Singapura', 'Quantidade (Kg)': '642', 'Valor (US$)': '5.235'}, {'Países': 'Suécia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Suíça', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Suriname', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Tailândia', 'Quantidade (Kg)': '17', 'Valor (US$)': '107'}, {'Países': 'Taiwan (Formosa)', 'Quantidade (Kg)': '901', 'Valor (US$)': '4.141'}, {'Países': 'Tcheca, República', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Trinidade e Tobago', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Turquia', 'Quantidade (Kg)': '2', 'Valor (US$)': '17'}, {'Países': 'Uruguai', 'Quantidade (Kg)': '10.200', 'Valor (US$)': '87.895'}, {'Países': 'Vanuatu', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Venezuela', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Vietnã', 'Quantidade (Kg)': '16', 'Valor (US$)': '19'}, {'Países': 'Outros(1)', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Total', 'Quantidade (Kg)': '929.865', 'Valor (US$)': '2.865.784'}]"                }
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
def getExports():
    processingURL = URL
    params = PROCESSING_PARAM

    year = request.args.get('year', default='', type=str)
    classification = request.args.get('classification', default='', type=str)

    if year:
        if not 1970 <= int(year) <= 2023:
            return jsonify({"message": "{Invalid Year, use a value between 1970 and 2023}"})
        yearParameter = f"ano={year}&"
        processingURL = f"{processingURL}{yearParameter}"
        params = f"{params}{year}"

    if classification: 
        classificationParameter = f"subopcao={classification}&"
        processingURL= f"{processingURL}{classificationParameter}"
        params = f"{params}{classification}"

    processingURL = f"{processingURL}{PROCESSING_PARAM}"

    data = scrape_page(processingURL, params)
    if "error" in data:
        return data
    return jsonify({"message": str(data)})
