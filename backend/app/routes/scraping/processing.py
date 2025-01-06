from flask import Blueprint, jsonify, request
from flasgger import swag_from
from app.routes.routes import URL
from app.services.scraping_service import scrape_page

PROCESSING_PARAM = 'opcao=opt_06' 

processing = Blueprint('processing', __name__)

@processing.route('/api/processing/', methods=['GET'])
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
