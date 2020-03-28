class InvalidRequestException(Exception):
    status_code = 400

    def __init__(self, error):
        message = 'Invalid request: {0}'.format(error)
        Exception.__init__(self, message)
