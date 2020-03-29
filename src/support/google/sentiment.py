import os
import json
from typing import Tuple
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from google.oauth2 import service_account


GLOBAL_API_CLIENT = None


def analyze_text(raw_text: str) -> Tuple[float, float]:
    """
    Uses Google sentiment analysis to analyze text

    :param raw_text: raw text to send for analysis
    :return: (sentiment.score, sentiment.magnitude)
    """
    global GLOBAL_API_CLIENT
    if GLOBAL_API_CLIENT is None:
        credentials = service_account.Credentials.from_service_account_info(json.loads(os.environ['GOOGLE_APPLICATION_CREDENTIALS']))
        GLOBAL_API_CLIENT = language.LanguageServiceClient(credentials=credentials)

    try:
        document = types.Document(
            content=raw_text,
            type=enums.Document.Type.PLAIN_TEXT)
        sentiment = GLOBAL_API_CLIENT.analyze_sentiment(document=document).document_sentiment
        return sentiment.score, sentiment.magnitude
    except:
        return 0, 0
