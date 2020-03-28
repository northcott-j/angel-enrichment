from dotenv import load_dotenv
from os import environ

flask_env = environ.get('FLASK_ENV', None)
if flask_env not in ['heroku', 'deploying']:
    load_dotenv()
