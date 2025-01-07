from flask import Blueprint, jsonify, request
from flasgger import swag_from
from app.routes.routes import URL
from app.services.scraping_service import scrape_page

COMERCE_PARAM = 'opcao=opt_04' 

comerce = Blueprint('comerce', __name__)

@comerce.route('/api/comerce/', methods=['GET'])
@swag_from({
    'tags': ['Comerce Wine Scraping'],
    'description': 'Endpoint que realiza web scraping em uma página de comercialização de vinhos, retornando informações sobre vinhos de um ano especificado.',
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
        }
    ],
    'responses': {
        200: {
            'description': 'Sucesso - Informações sobre os vinhos retornadas.',
            'content': {
                'application/json': {
                    "message": "[{'Produto': 'VINHO DE MESA', 'Quantidade (L.)': '187.939.996'}, {'Produto': 'Tinto', 'Quantidade (L.)': '165.067.340'}, {'Produto': 'Rosado', 'Quantidade (L.)': '2.213.723'}, {'Produto': 'Branco', 'Quantidade (L.)': '20.658.933'}, {'Produto': 'VINHO FINO DE MESA', 'Quantidade (L.)': '21.533.487'}, {'Produto': 'Tinto', 'Quantidade (L.)': '15.258.778'}, {'Produto': 'Rosado', 'Quantidade (L.)': '1.318.396'}, {'Produto': 'Branco', 'Quantidade (L.)': '4.956.314'}, {'Produto': 'VINHO FRIZANTE', 'Quantidade (L.)': '2.875.864'}, {'Produto': 'VINHO ORGÂNICO', 'Quantidade (L.)': '14.947'}, {'Produto': 'VINHO ESPECIAL', 'Quantidade (L.)': '-'}, {'Produto': 'Tinto', 'Quantidade (L.)': '-'}, {'Produto': 'Rosado', 'Quantidade (L.)': '-'}, {'Produto': 'Branco', 'Quantidade (L.)': '-'}, {'Produto': 'ESPUMANTES', 'Quantidade (L.)': '29.525.942'}, {'Produto': 'Espumante  Moscatel', 'Quantidade (L.)': '12.204.315'}, {'Produto': 'Espumante', 'Quantidade (L.)': '17.321.031'}, {'Produto': 'Espumante Orgânico', 'Quantidade (L.)': '597'}, {'Produto': 'SUCO DE UVAS', 'Quantidade (L.)': '157.125.036'}, {'Produto': 'Suco Natural Integral', 'Quantidade (L.)': '115.394.795'}, {'Produto': 'Suco Adoçado', 'Quantidade (L.)': '-'}, {'Produto': 'Suco Reprocessado/reconstituido', 'Quantidade (L.)': '35.139.154'}, {'Produto': 'Suco Orgânico', 'Quantidade (L.)': '1.002.685'}, {'Produto': 'Outros sucos de uvas', 'Quantidade (L.)': '5.588.403'}, {'Produto': 'SUCO DE UVAS CONCENTRADO', 'Quantidade (L.)': '33.632.834'}, {'Produto': 'OUTROS PRODUTOS COMERCIALIZADOS', 'Quantidade (L.)': '31.704.382'}, {'Produto': 'Outros vinhos (sem informação detalhada)', 'Quantidade (L.)': '8.812'}, {'Produto': 'Agrin (fermentado, acetico misto)', 'Quantidade (L.)': '-'}, {'Produto': 'Aguardente de vinho 50°gl', 'Quantidade (L.)': '-'}, {'Produto': 'Alcool vinico', 'Quantidade (L.)': '-'}, {'Produto': 'Bagaceira (graspa)', 'Quantidade (L.)': '5.594'}, {'Produto': 'Base champenoise champanha', 'Quantidade (L.)': '60.958'}, {'Produto': 'Base charmat champanha', 'Quantidade (L.)': '226.901'}, {'Produto': 'Base espumante moscatel', 'Quantidade (L.)': '720.603'}, {'Produto': 'Bebida de uva', 'Quantidade (L.)': '139.943'}, {'Produto': 'Borra líquida', 'Quantidade (L.)': '49.840'}, {'Produto': 'Borra seca', 'Quantidade (L.)': '122.525'}, {'Produto': 'Brandy (conhaque)', 'Quantidade (L.)': '4.407'}, {'Produto': 'Cooler', 'Quantidade (L.)': '4.505.384'}, {'Produto': 'Coquetel com vinho', 'Quantidade (L.)': '292.420'}, {'Produto': 'Destilado de vinho', 'Quantidade (L.)': '33'}, {'Produto': 'Filtrado doce', 'Quantidade (L.)': '2.339.403'}, {'Produto': 'Jeropiga', 'Quantidade (L.)': '1.392'}, {'Produto': 'Mistelas', 'Quantidade (L.)': '4.080'}, {'Produto': 'Mosto concentrado', 'Quantidade (L.)': '-'}, {'Produto': 'Mosto de uva', 'Quantidade (L.)': '1.579.638'}, {'Produto': 'Mosto sulfitado', 'Quantidade (L.)': '-'}, {'Produto': 'Nectar de uva', 'Quantidade (L.)': '4.719.055'}, {'Produto': 'Outros produtos', 'Quantidade (L.)': '7.406.812'}, {'Produto': 'Polpa de uva', 'Quantidade (L.)': '1.058.011'}, {'Produto': 'Preparado líquido para refresco', 'Quantidade (L.)': '19.711'}, {'Produto': 'Refrigerante +50% suco', 'Quantidade (L.)': '265.026'}, {'Produto': 'Sangria', 'Quantidade (L.)': '95.605'}, {'Produto': 'Vinagre balsamico', 'Quantidade (L.)': '296.664'}, {'Produto': 'Vinagre duplo', 'Quantidade (L.)': '987.142'}, {'Produto': 'Vinagre simples', 'Quantidade (L.)': '5.309.881'}, {'Produto': 'Vinho acetificado', 'Quantidade (L.)': '1.052.563'}, {'Produto': 'Vinho base para espumantes', 'Quantidade (L.)': '-'}, {'Produto': 'Vinho composto', 'Quantidade (L.)': '32.000'}, {'Produto': 'Vinho licoroso', 'Quantidade (L.)': '385.006'}, {'Produto': 'Vinho leve', 'Quantidade (L.)': '27'}, {'Produto': 'Vinho gaseificado', 'Quantidade (L.)': '14.947'}, {'Produto': 'Total', 'Quantidade (L.)': '464.352.488'}]"
                }
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
def getComerce():
    comerceURL = URL
    params = COMERCE_PARAM

    year = request.args.get('year', default='', type=str)
    if year:
        if not 1970 <= int(year) <= 2023:
            return jsonify({"message": "{Invalid Year, use a value between 1970 and 2023}"})
        yearParameter = f"ano={year}&"
        comerceURL = f"{comerceURL}{yearParameter}"
        params = f"{params}{year}"


    comerceURL = f"{comerceURL}{COMERCE_PARAM}" 
    
    data = scrape_page(comerceURL, params)
    if "error" in data:
        return data
    return jsonify({"message": str(data)})

