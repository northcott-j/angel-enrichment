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

app.register_blueprint(typeform, url_prefix='/typeform')


# Unauthenticated heartbeat to see if this is alive
@app.route('/', methods=['GET'])
def heartbeat():
    return "Hello there."
