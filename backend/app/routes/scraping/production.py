from flask import Blueprint, jsonify, request
from flasgger import swag_from
from app.routes.routes import URL
from app.services.scraping_service import scrape_page

PRODUCTION_PARAM = 'opcao=opt_02' 

production = Blueprint('production', __name__)

@production.route('/api/production/', methods=['GET'])
@swag_from({
    'tags': ['Production Wine Scraping'],
    'description': 'Endpoint que realiza web scraping em uma página de produção de vinhos, retornando informações sobre vinhos de um ano especificado.',
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
                    "message": "[{'Produto': 'VINHO DE MESA', 'Quantidade (L.)': '124.200.414'}, {'Produto': 'Tinto', 'Quantidade (L.)': '103.916.391'}, {'Produto': 'Branco', 'Quantidade (L.)': '19.568.734'}, {'Produto': 'Rosado', 'Quantidade (L.)': '715.289'}, {'Produto': 'VINHO FINO DE MESA (VINIFERA)', 'Quantidade (L.)': '32.516.686'}, {'Produto': 'Tinto', 'Quantidade (L.)': '15.451.883'}, {'Produto': 'Branco', 'Quantidade (L.)': '15.487.915'}, {'Produto': 'Rosado', 'Quantidade (L.)': '1.576.888'}, {'Produto': 'SUCO', 'Quantidade (L.)': '69.261.287'}, {'Produto': 'Suco de uva integral', 'Quantidade (L.)': '40.718.523'}, {'Produto': 'Suco de uva concentrado', 'Quantidade (L.)': '27.963.865'}, {'Produto': 'Suco de uva adoçado', 'Quantidade (L.)': '107.289'}, {'Produto': 'Suco de uva orgânico', 'Quantidade (L.)': '471.610'}, {'Produto': 'Suco de uva reconstituído', 'Quantidade (L.)': '-'}, {'Produto': 'DERIVADOS', 'Quantidade (L.)': '92.533.804'}, {'Produto': 'Espumante', 'Quantidade (L.)': '32.399'}, {'Produto': 'Espumante moscatel', 'Quantidade (L.)': '689.139'}, {'Produto': 'Base espumante', 'Quantidade (L.)': '-'}, {'Produto': 'Base espumante moscatel', 'Quantidade (L.)': '3.006.705'}, {'Produto': 'Base Champenoise champanha', 'Quantidade (L.)': '200.777'}, {'Produto': 'Base Charmat champanha', 'Quantidade (L.)': '2.487.939'}, {'Produto': 'Bebida de uva', 'Quantidade (L.)': '-'}, {'Produto': 'Polpa de uva', 'Quantidade (L.)': '1.803.472'}, {'Produto': 'Mosto simples', 'Quantidade (L.)': '80.355.474'}, {'Produto': 'Mosto concentrado', 'Quantidade (L.)': '-'}, {'Produto': 'Mosto de uva com bagaço', 'Quantidade (L.)': '3.078.256'}, {'Produto': 'Mosto dessulfitado', 'Quantidade (L.)': '5.000'}, {'Produto': 'Mistelas', 'Quantidade (L.)': '-'}, {'Produto': 'Néctar de uva', 'Quantidade (L.)': '46.000'}, {'Produto': 'Licorosos', 'Quantidade (L.)': '-'}, {'Produto': 'Compostos', 'Quantidade (L.)': '-'}, {'Produto': 'Jeropiga', 'Quantidade (L.)': '2.000'}, {'Produto': 'Filtrado', 'Quantidade (L.)': '-'}, {'Produto': 'Frisante', 'Quantidade (L.)': '-'}, {'Produto': 'Vinho leve', 'Quantidade (L.)': '-'}, {'Produto': 'Vinho licoroso', 'Quantidade (L.)': '48.678'}, {'Produto': 'Brandy', 'Quantidade (L.)': '-'}, {'Produto': 'Destilado', 'Quantidade (L.)': '-'}, {'Produto': 'Bagaceira', 'Quantidade (L.)': '-'}, {'Produto': 'Licor de bagaceira', 'Quantidade (L.)': '5.800'}, {'Produto': 'Vinagre', 'Quantidade (L.)': '10.000'}, {'Produto': 'Borra líquida', 'Quantidade (L.)': '509.378'}, {'Produto': 'Borra seca', 'Quantidade (L.)': '167.587'}, {'Produto': 'Vinho Composto', 'Quantidade (L.)': '-'}, {'Produto': 'Pisco', 'Quantidade (L.)': '1.000'}, {'Produto': 'Vinho orgânico', 'Quantidade (L.)': '18.700'}, {'Produto': 'Espumante orgânico', 'Quantidade (L.)': '-'}, {'Produto': 'Destilado alcoólico simples de bagaceira', 'Quantidade (L.)': '500'}, {'Produto': 'Vinho acidificado', 'Quantidade (L.)': '65.000'}, {'Produto': 'Mosto parcialmente fermentado', 'Quantidade (L.)': '-'}, {'Produto': 'Outros derivados', 'Quantidade (L.)': '-'}, {'Produto': 'Total', 'Quantidade (L.)': '318.512.191'}]"                }
            }
        },
        400: {
            'description': 'Requisição inválida - Ano informado fora do período aceitado',
            'content': {
                'application/json': {
                        "message": "{Invalid Year, use a value between 1970 and 2023}"
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
def getProduction():
    productionURL = URL
    params = PRODUCTION_PARAM

    year = request.args.get('year', default='', type=str)
    
    if year:
        if not 1970 <= int(year) <= 2023:
            return jsonify({"message": "{Invalid Year, use a value between 1970 and 2023}"})
        yearParameter = f"ano={year}&"
        productionURL = f"{productionURL}{yearParameter}"
        params = f"{params}{year}"

    productionURL = f"{productionURL}{PRODUCTION_PARAM}" 
    data = scrape_page(productionURL, params)
    if "error" in data:
        return data
    return jsonify({"message": str(data)})

