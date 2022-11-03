from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

# make a db object and a migrate object
# migration talks about taking ourselves from an empty database to a db that has the schema, table and relations that we want
# migrate object helps us create these rules
db = SQLAlchemy()
migrate = Migrate()
load_dotenv()
# the above makes the variables in .env file available as environment variables
# available in form of dictionary
# have to check whether we are testing or not to choose correct config
# alter the param of create_app below to only run when testing=None

def create_app(testing=None):
    # must be named exactly this becuase we will be running through flask on the command line. 
    # flask will look specifically for a create_app function, in the __init__.py in the app folder in the root directory
    # __name__ stores the name of the module we're in
    app = Flask(__name__)
    # need to do the above

    # part of sqlalchemy boilerplate:
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # where is my postgres database on the my computer? later, on the internet
    # postgres:postgres refers to username:password
    if testing is None:
        app.config["SQLALCHEMY_DATABASE_URI"]=os.environ.get("SQLALCHEMY_DATABASE_URI")
    #app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:postgres@localhost:5432/bikes_development"
    # changes the above so that it is not hard coded
    # to make code more flexible --> using .env file and configs
    # in the case where we are testing:
    else:
        # app.config["TESTING"]=True
        app.config["SQLALCHEMY_DATABASE_URI"]=os.environ.get("SQLALCHEMY_TEST_DATABASE_URI")

    # import Bike model
    # must do this before the next two lines or else migrate won't be able to import it
    from app.models.bike import Bike

    # where you connect the database to the app:
    db.init_app(app)
    # and the migrate object to the app and database
    migrate.init_app(app,db)


    # configuration
    # we need to have the import inside the funciton for routes
    # no circular dependency, python knows to import global first
    from .routes.bike import bike_bp
    # now we need to register the blueprint and tell python it exists
    app.register_blueprint(bike_bp)

    return app
    # need to do the above