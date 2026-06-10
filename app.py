from flask import Flask
from flask_cors import CORS
from config import Config
from qr_app.routes import routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    app.register_blueprint(routes)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
