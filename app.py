import json
from waitress import serve
from pyramid.config import Configurator
from pyramid.response import Response
from scraper import *

handelProcess()

def fuel_prices(request):
    print('Incoming request')
    fuelPrice = getFuelPrices()
    print(request)
    try:
        requestQuery = str(request).split(' HTTP/1.1')[0].split('?')[1]
        parameters = requestQuery.split('=')
        parameters[1] = parameters[1].replace('-',' ')
        fuelData = { "Country Found": False }
        for value in fuelPrice['fuelPrices']:
            if (parameters[1].lower().find("all") >= 0):
                fuelData = fuelPrice
            elif( value['country'].lower().find(parameters[1].lower()) >= 0):
                fuelData = {
                    "country": value['country'],
                    "petrol": value['petrol'],
                    "diesel": value['diesel'],
                    "currency": value['currency'],
                }
        
        if parameters[1].find("&") >= 0:
            return { 
                "Error": 404,
                "Required Content Type": "application/json",
                "Description": "For all countries please add the JSON that is inside the body tag below or add a single parameter shown below",
                "Body": [
                    {
                        "country": "all"
                    }
                ],
                "Parameter": "https://api.aws.xander.pro/european-fuel?country=all"
            }
        else:
            return fuelData
    except:
        try:
            requestbody = request.body
            bodyJson = json.loads(requestbody)
            fuelData = { "Country Found": False }

            for value in fuelPrice['fuelPrices']:
                if (bodyJson['country'].lower().find("all") >= 0):
                    fuelData = fuelPrice
                elif( value['country'].lower().find(bodyJson['country'].lower()) >= 0):
                    fuelData = {
                        "country": value['country'],
                        "petrol": value['petrol'],
                        "diesel": value['diesel'],
                        "currency": value['currency'],
                    }

            return fuelData
        except:
            return { 
                "Error": 404,
                "Required Content Type": "application/json",
                "Description": "For all countries please add the JSON that is inside the body tag below or add a single parameter shown below",
                "Body": [
                    {
                        "country": "all"
                    }
                ],
                "Parameter": "https://api.aws.xander.pro/european-fuel?country=all"
            }


if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('fuel', '/european-fuel')
        config.add_view(fuel_prices, route_name='fuel', request_method='GET', renderer='json')
        app = config.make_wsgi_app()
    serve(app, host='0.0.0.0', port=3000)