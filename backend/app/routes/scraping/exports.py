from flask import Blueprint, jsonify, request
from flasgger import swag_from
from app.routes.routes import URL
from app.services.scraping_service import scrape_page

EXPORTS_PARAM = 'opcao=opt_06' 

exports = Blueprint('exports', __name__)

@exports.route('/api/exports/', methods=['GET'])
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
