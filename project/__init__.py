from flask import Flask
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)

    from . import _config
    app.config['SQLALCHEMY_DATABASE_URI'] = _config.connection_string
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    @app.route("/")
    def index():
        return "Hello, PetFax!"
    
    from . import (pet, fact)
    app.register_blueprint(pet.bp)
    app.register_blueprint(fact.bp)
    
    return app