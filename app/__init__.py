from flask import Flask

def create_app():
    # must be named exactly this becuase we will be running through flask on the command line. 
    # flask will look specifically for a create_app function, in the __init__.py in the app folder in the root directory
    # __name__ stores the name of the module we're in
    app = Flask(__name__)
    # need to do the above


    # configuration
    # we need to have the import inside the funciton for routes
    # no circular dependency, python knows to import global first
    from .routes.bike import bike_bp
    # now we need to register the blueprint and tell python it exists
    app.register_blueprint(bike_bp)

    return app
    # need to do the above