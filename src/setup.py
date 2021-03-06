import os
from flask_cors import CORS
from flask import Flask
from .config import DevelopmentConfig, ProductionConfig

# Creating Flask application
app = Flask(__name__)

# Initializing config
mode = os.environ.get('FLASK_ENV', None)

if mode == 'development':
    app.config.from_object(DevelopmentConfig)
else:
    app.config.from_object(ProductionConfig)


# Allow CORS
CORS(app, supports_credentials=True)

# Initialize Controllers
from .controllers.typeform import typeform
from .controllers.resources import resources
from .controllers.analysis import analysis

app.register_blueprint(typeform, url_prefix='/typeform')
app.register_blueprint(resources, url_prefix='/resources')
app.register_blueprint(analysis, url_prefix='/analysis')


# Unauthenticated heartbeat to see if this is alive
@app.route('/', methods=['GET'])
def heartbeat():
    return "Hello there."
