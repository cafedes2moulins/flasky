import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.bike import Bike


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()



#  prepopulates db
@pytest.fixture
def two_bikes(app):
    # app is used within the context of our test, not directly in the fixture
    # we pass it in to ensure we are refering tot he same test client in every case
    bike1 = Bike("Edison", 600, 43, "electric")
    bike2 = Bike("Giant", 700, 50, "hybrid")

    db.session.add(bike1)
    db.session.add(bike2)
    db.session.commit()
