from flask import Blueprint, jsonify, request
from flasgger import swag_from
from app.routes.routes import URL
from app.services.scraping_service import scrape_page

COMERCE_PARAM = 'opcao=opt_04' 

comerce = Blueprint('comerce', __name__)

@comerce.route('/api/comerce/', methods=['GET'])
def getComerce():
    comerceURL = URL
    params = COMERCE_PARAM

    year = request.args.get('year', default='', type=str)
    if year:
        if 1970 < int(year) > 2023:
            return jsonify({"message": "Invalid Year, use a value between 1970 and 2023"})
        yearParameter = f"?ano={year}&"
        comerceURL = f"{comerceURL}{yearParameter}"
        params = f"{params}{year}"


    comerceURL = f"{comerceURL}{COMERCE_PARAM}" 
    
    data = scrape_page(comerceURL, params)
    if "error" in data:
        return data
    print(data)
    return jsonify({"message": str(data)})

