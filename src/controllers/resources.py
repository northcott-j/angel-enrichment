from flask import Blueprint, jsonify, request
from src.support.resources import get_resource


resources = Blueprint('resources', __name__)


@resources.route('/', methods=['GET'])
def get_resources():
    """
    Get a resource based on: location, age, and type of trafficking

    :return: sends back a list of resources
    """
    country = request.args.get('country')
    if country: country = f'country:{country.lower().replace(" ", "-")}'
    state = request.args.get('state')
    if state: state = f'state:{state.lower().replace(" ", "-")}'
    city = request.args.get('city')
    if city: city = f'city:{city.lower().replace(" ", "-")}'
    age = request.args.get('age')
    traffic_type = request.args.get('traffic_type')
    try:
        inclusive = bool(int(request.args.get('inclusive', 1)))
    except:
        inclusive = True
    return jsonify(get_resource(country=country, state=state, city=city, age=age, traffic_type=traffic_type, inclusive=inclusive))
