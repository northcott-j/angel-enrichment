from flask import Blueprint, jsonify, request
from typing import Dict
from src.support import inject_request_body

typeform = Blueprint('typeform', __name__)


@typeform.route('response', methods=['POST'])
@inject_request_body()
def response_webhook(data: Dict):
    """
    Handles a webhook response from typeform

    :param data: injected request body that contains needed query info
    :return: sends an email and logs information
    """
    print(data)
    return jsonify('i got it!!!')


@typeform.route('redirect', methods=['GET'])
def typeform_redirect():
    """
    Temporary capture of the redirect form. Final redirect will be handled by UI

    :return: logs the request
    """
    print(request.args)
    return jsonify(request.args)
