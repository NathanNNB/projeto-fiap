from flask import Blueprint, jsonify, request
from flasgger import swag_from
from app.routes.routes import URL
from app.services.scraping_service import scrape_page

EXPORTS_PARAM = 'opcao=opt_06' 

exports = Blueprint('exports', __name__)

@exports.route('/api/exports/', methods=['GET'])
@swag_from({
    'tags': ['Exports Wine Scraping'],
    'description': 'Endpoint que realiza web scraping em uma página de exportação de vinhos, retornando informações sobre vinhos de um ano especificado.',
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
                'enum': ['subopt_01', 'subopt_02', 'subopt_03', 'subopt_04' ],
                'example': 'subopt_02'
            }
        },
    ],
    'responses': {
        200: {
            'description': 'Sucesso - Informações sobre os vinhos retornadas.',
            'content': {
                'application/json': {
                    "message": "[{'Países': 'África do Sul', 'Quantidade (Kg)': '2', 'Valor (US$)': '44'}, {'Países': 'Alemanha', 'Quantidade (Kg)': '162', 'Valor (US$)': '1.542'}, {'Países': 'Angola', 'Quantidade (Kg)': '56.242', 'Valor (US$)': '315.073'}, {'Países': 'Antigua e Barbuda', 'Quantidade (Kg)': '24', 'Valor (US$)': '100'}, {'Países': 'Antilhas Holandesas', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Argentina', 'Quantidade (Kg)': '8.593', 'Valor (US$)': '73.239'}, {'Países': 'Aruba', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Australia', 'Quantidade (Kg)': '10', 'Valor (US$)': '6'}, {'Países': 'Bahamas', 'Quantidade (Kg)': '65', 'Valor (US$)': '268'}, {'Países': 'Bangladesh', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Barbados', 'Quantidade (Kg)': '32', 'Valor (US$)': '219'}, {'Países': 'Belgica', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Benin', 'Quantidade (Kg)': '3', 'Valor (US$)': '19'}, {'Países': 'Bermudas', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Bolívia', 'Quantidade (Kg)': '11.410', 'Valor (US$)': '34.481'}, {'Países': 'Bósnia-Herzegovina', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Bulgaria', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Cabo Verde', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Camarões', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Canada', 'Quantidade (Kg)': '4.068', 'Valor (US$)': '15.427'}, {'Países': 'Catar', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Cayman, Ilhas', 'Quantidade (Kg)': '5', 'Valor (US$)': '33'}, {'Países': 'Chile', 'Quantidade (Kg)': '3.532', 'Valor (US$)': '15.875'}, {'Países': 'China', 'Quantidade (Kg)': '16.285', 'Valor (US$)': '47.822'}, {'Países': 'Chipre', 'Quantidade (Kg)': '188', 'Valor (US$)': '707'}, {'Países': 'Cingapura', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Colombia', 'Quantidade (Kg)': '1.926', 'Valor (US$)': '6.898'}, {'Países': 'Coreia do Sul, Republica da', 'Quantidade (Kg)': '74', 'Valor (US$)': '222'}, {'Países': 'Costa Rica', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Cuba', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Curaçao', 'Quantidade (Kg)': '1.288', 'Valor (US$)': '6.539'}, {'Países': 'Dinamarca', 'Quantidade (Kg)': '2.790', 'Valor (US$)': '26.359'}, {'Países': 'Dominica', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'El Salvador', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Emirados Arabes Unidos', 'Quantidade (Kg)': '126', 'Valor (US$)': '622'}, {'Países': 'Equador', 'Quantidade (Kg)': '540', 'Valor (US$)': '2.000'}, {'Países': 'Espanha', 'Quantidade (Kg)': '45', 'Valor (US$)': '853'}, {'Países': 'Estados Unidos', 'Quantidade (Kg)': '255.198', 'Valor (US$)': '729.055'}, {'Países': 'Estonia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Falkland (Malvinas)', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Filipinas', 'Quantidade (Kg)': '20', 'Valor (US$)': '111'}, {'Países': 'Filânldia', 'Quantidade (Kg)': '180', 'Valor (US$)': '1.770'}, {'Países': 'França', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Gana', 'Quantidade (Kg)': '4.719', 'Valor (US$)': '35.778'}, {'Países': 'Gibraltar', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Granada', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Grécia', 'Quantidade (Kg)': '59', 'Valor (US$)': '320'}, {'Países': 'Guatemala', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Guiana', 'Quantidade (Kg)': '14.084', 'Valor (US$)': '71.163'}, {'Países': 'Guiné Equatorial', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Guiné-Bissau', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Haiti', 'Quantidade (Kg)': '3.969', 'Valor (US$)': '10.646'}, {'Países': 'Honduras', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Hong Kong', 'Quantidade (Kg)': '1.355', 'Valor (US$)': '5.169'}, {'Países': 'Hungria', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Ilha de Man', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Índia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Iraque', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Irlanda', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Islândia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Itália', 'Quantidade (Kg)': '1.460', 'Valor (US$)': '19.905'}, {'Países': 'Japão', 'Quantidade (Kg)': '2.311', 'Valor (US$)': '9.708'}, {'Países': 'Jordânia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Letônia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Líbano', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Libéria', 'Quantidade (Kg)': '973', 'Valor (US$)': '3.358'}, {'Países': 'Luxemburgo', 'Quantidade (Kg)': '18', 'Valor (US$)': '305'}, {'Países': 'Maldivas', 'Quantidade (Kg)': '4.577', 'Valor (US$)': '20.204'}, {'Países': 'Malta', 'Quantidade (Kg)': '1.472', 'Valor (US$)': '44.498'}, {'Países': 'Marshall, Ilhas', 'Quantidade (Kg)': '1.375', 'Valor (US$)': '4.886'}, {'Países': 'Montenegro', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'México', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Nicarágua', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Nigéria', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Noruega', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Nova Zelândia', 'Quantidade (Kg)': '303', 'Valor (US$)': '4.231'}, {'Países': 'Países Baixos (Holanda)', 'Quantidade (Kg)': '3', 'Valor (US$)': '49'}, {'Países': 'Panamá', 'Quantidade (Kg)': '7.936', 'Valor (US$)': '43.115'}, {'Países': 'Paraguai', 'Quantidade (Kg)': '64.662', 'Valor (US$)': '192.975'}, {'Países': 'Peru', 'Quantidade (Kg)': '108', 'Valor (US$)': '756'}, {'Países': 'Polônia', 'Quantidade (Kg)': '126', 'Valor (US$)': '659'}, {'Países': 'Porto Rico', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Portugal', 'Quantidade (Kg)': '2.191', 'Valor (US$)': '38.616'}, {'Países': 'Quênia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Reino Unido', 'Quantidade (Kg)': '16.057', 'Valor (US$)': '86.879'}, {'Países': 'Republica Dominicana', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Republica Tcheca', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Rússia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Serra Leoa', 'Quantidade (Kg)': '271', 'Valor (US$)': '1.287'}, {'Países': 'Singapura', 'Quantidade (Kg)': '209', 'Valor (US$)': '599'}, {'Países': 'Suécia', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Suíça', 'Quantidade (Kg)': '444', 'Valor (US$)': '4.474'}, {'Países': 'Suriname', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Tailândia', 'Quantidade (Kg)': '7', 'Valor (US$)': '43'}, {'Países': 'Taiwan (Formosa)', 'Quantidade (Kg)': '1.099', 'Valor (US$)': '3.664'}, {'Países': 'Tcheca, República', 'Quantidade (Kg)': '167', 'Valor (US$)': '1.236'}, {'Países': 'Trinidade e Tobago', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Turquia', 'Quantidade (Kg)': '6.930', 'Valor (US$)': '26.566'}, {'Países': 'Uruguai', 'Quantidade (Kg)': '2.812', 'Valor (US$)': '14.352'}, {'Países': 'Vanuatu', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Venezuela', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Vietnã', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Outros(1)', 'Quantidade (Kg)': '-', 'Valor (US$)': '-'}, {'Países': 'Total', 'Quantidade (Kg)': '502.505', 'Valor (US$)': '1.924.725'}]"}
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
    exportsURL = URL
    params = EXPORTS_PARAM

    year = request.args.get('year', default='', type=str)
    classification = request.args.get('classification', default='', type=str)

    if year:
        if not 1970 <= int(year) <= 2023:
            return jsonify({"message": "{Invalid Year, use a value between 1970 and 2023}"})
        yearParameter = f"ano={year}&"
        exportsURL = f"{exportsURL}{yearParameter}"
        params = f"{params}{year}"

    if classification: 
        classificationParameter = f"subopcao={classification}&"
        exportsURL= f"{exportsURL}{classificationParameter}"
        params = f"{params}{classification}"

    exportsURL = f"{exportsURL}{EXPORTS_PARAM}" 
    data = scrape_page(exportsURL, params)
    if "error" in data:
        return data
    return jsonify({"message": str(data)})
