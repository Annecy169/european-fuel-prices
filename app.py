import json
from waitress import serve
from pyramid.config import Configurator
from pyramid.response import Response
from scraper import *

handelProcess()

def fuel_prices(request):
    print('Incoming request')
    fuelPrice = getFuelPrices()
    try:
        requestbody = request.body
        bodyJson = json.loads(requestbody)
        print(bodyJson['country'])
        return bodyJson['country']
    except:
        return fuelPrice


if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('fuel', '/')
        config.add_view(fuel_prices, route_name='fuel', request_method='GET', renderer='json')
        app = config.make_wsgi_app()
    serve(app, host='0.0.0.0', port=3032)