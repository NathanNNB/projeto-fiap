from flask import Blueprint, jsonify, request
from flasgger import swag_from
from app.routes.routes import URL
from app.services.scraping_service import scrape_page

PROCESSING_PARAM = 'opcao=opt_03' 

processing = Blueprint('processing', __name__)

@processing.route('/api/processing', methods=['GET'])
def hello():
    return jsonify({"message": "Olá, processing!"})

@processing.route('/api/processing/processing', methods=['GET'])
def getProcessing():
    processingURL = URL
    params = PROCESSING_PARAM

    year = request.args.get('year', default='', type=str)
    if year:
        if 1970 < int(year) > 2023:
            return jsonify({"message": "Invalid Year, use a value between 1970 and 2023"})
        yearParameter = f"?ano={year}"
        processingURL = f"{processingURL}{yearParameter}"
        params = f"{params}{year}"


    processingURL = f"{processingURL}&{PROCESSING_PARAM}" 
    
    data = scrape_page(processingURL, params)
    if "error" in data:
        return data
    print(data)
    return jsonify({"message": str(data)})

