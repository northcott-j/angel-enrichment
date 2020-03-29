import json
from os import getcwd, path
from typing import List, Union, Dict


def get_resource(country: str = None, state: str = None, city: str = None,
                 age: str = None, traffic_type: Union[List[str], str] = None,
                 inclusive: bool = True) -> List[Dict[str, str]]:
    """
    Fetches resources from storage (json for right now)

    :param country: country level resources
    :param state: state level resources
    :param city: city level resources
    :param age: adult or child or general or all (or comma separated)
    :param traffic_type: sex or labor or or general or all (or comma separated)
    :param inclusive: include all resources up to international level or just the closest to home
    :return: list of applicable resources
    """
    age = set() if age is None else {a.strip() for a in age.split(',')}
    traffic_type = set() if traffic_type is None else {t.strip() for t in traffic_type.split(',')}
    kwargs = {'country': country, 'state': state, 'city': city,
              'ages': {'child', 'adult', 'general'} if 'all' in age else age,
              'traffic_types': {'sex', 'labor', 'general'} if 'all' in traffic_type else traffic_type}
    resources = []
    geo_order = ['city', 'state', 'country', 'international']
    if inclusive:
        kwargs['ages'].add('general')
        kwargs['traffic_types'].add('general')
    with open(__storage_path(), 'r') as infile:
        data = json.load(infile)
    for geo in geo_order:
        # NOTE :: Get the data for this geo level
        data_key = kwargs.get(geo) if geo != 'international' else 'international'
        geo_data = data.get(data_key, {})
        found_geo_data = False
        if geo_data:
            found_geo_data = True
            # NOTE :: If age or traffic_type were passed
            for age in kwargs['ages']:
                geo_age_data = geo_data.get(age, {})
                if geo_age_data:
                    for traffic_type in kwargs['traffic_types']:
                        resources.extend(geo_age_data.get(traffic_type, []))
        if not inclusive and found_geo_data: break
    return resources


def __storage_path() -> str:
    return path.join(getcwd(), 'src', 'support', 'resources', 'resources.json')
