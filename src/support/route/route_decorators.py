from flask import request
from functools import wraps
from src.support.exceptions import InvalidRequestException


def parametrized(dec):
    """
    Decorator to allow a decorator to support parameters

    :param dec: decorator to decorate
    :return: decorated decorator that allows params
    """
    def layer(*args, **kwargs):
        def repl(f):
            return dec(f, *args, **kwargs)
        return repl
    return layer


@parametrized
def inject_request_body(f, **params):
    """
    Takes JSON body from POST request and passes it as a func param

    :param f: route to wrap
    :param params: parameters (allowed=filters out keys to be allowed in json)
    :return: decorated function injecting json body
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        data = request.get_json(force=True, silent=True)
        if data is None:
            raise InvalidRequestException('Expected a JSON request body!')

        if 'allowed' in params:
            data = {k: data[k] for k in params['allowed'] if k in data}

        kwargs['data'] = data
        return f(*args, **kwargs)

    return decorated
