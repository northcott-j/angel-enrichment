from flask import Blueprint, jsonify, request
from src.support.google import analyze_text


analysis = Blueprint('analysis', __name__)


@analysis.route('/sentiment', methods=['GET'])
def sentiment_analysis():
    """
    Get results for Google sentiment analysis

    TODO :: Swap this out to a POST when ready to use it

    :return: sends back a sentiment score
    """
    return jsonify(analyze_text(request.args.get('text', '')))
