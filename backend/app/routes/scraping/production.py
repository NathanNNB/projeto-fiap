from flask import Blueprint, jsonify, request
from flasgger import swag_from
from app.routes.routes import URL
from app.services.scraping_service import scrape_page

PRODUCTION_PARAM = 'opcao=opt_02' 

production = Blueprint('production', __name__)

@production.route('/api/production/', methods=['GET'])
def getProduction():
    productionURL = URL
    params = PRODUCTION_PARAM

    year = request.args.get('year', default='', type=str)
    if year:
        if 1970 < int(year) > 2023:
            return jsonify({"message": "Invalid Year, use a value between 1970 and 2023"})
        yearParameter = f"?ano={year}"
        productionURL = f"{productionURL}{yearParameter}"
        params = f"{params}{year}"


    productionURL = f"{productionURL}&{PRODUCTION_PARAM}" 
    print(productionURL)
    data = scrape_page(productionURL, params)
    if "error" in data:
        return data
    return jsonify({"message": str(data)})

