from flask import Flask 

def create_app(): 
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@127.0.0.1:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False     

    @app.route('/')
    def hello(): 
        return 'Hello, PetFax!'

    # register pet blueprint
    from . import pet
    app.register_blueprint(pet.bp)

    from . import fact
    app.register_blueprint(fact.bp)

    return app
