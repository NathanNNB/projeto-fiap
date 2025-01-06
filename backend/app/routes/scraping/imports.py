from flask import Blueprint, jsonify, request
from flasgger import swag_from
from app.routes.routes import URL
from app.services.scraping_service import scrape_page

IMPORTS_PARAM = 'opcao=opt_05' 

imports = Blueprint('imports', __name__)

@imports.route('/api/imports/', methods=['GET'])
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


