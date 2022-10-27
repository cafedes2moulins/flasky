from flask import Blueprint, jsonify, request
from app import db
from app.models.bike import Bike



bike_bp = Blueprint("bike_bp", __name__, url_prefix="/bike")

# # when a request comes in for this prefix, this is the response that I want you to use
# # empty "", or an addition to the route -->  "/features"
# # and a list for what methods that we want this response to be used for 
# @bike_bp.route("", methods=["GET"])
# def get_all_bikes():
#     #this returns the JSON that will actually be returned to the client

#     # we need to convert our python class into json
#     #first we must convert to a dictionary, then jsonify can turn it into JSON
#     response = []
#     for bike in bikes:
#         bike_dict = {
#             "id": bike.id,
#             "name": bike.name,
#             "price": bike.price,
#             "size": bike.size,
#             "type": bike.type
#         }
#         response.append(bike_dict)

#     # have to jsonify the return
#     # response body followed by the status code
#     return jsonify(response), 200
#     # whatever gets returned here is the response the the request determined 
#     # above in the decorator and blueprint

# # angular brackets indicate a parameter that a user has to specify
# @bike_bp.route("/<bike_id>", methods = ["GET"])
# def get_specific_bike(bike_id):
#     try:
#         verified_id = int(bike_id)
#     except ValueError:
#         return jsonify("Invalid ID: id must be an integer"), 400

#     for bike in bikes:
#         if bike.id == verified_id:
#             bike_dict = {
#                 "id": bike.id,
#                 "name": bike.name,
#                 "price": bike.price,
#                 "size": bike.size,
#                 "type": bike.type
#             }
#             return jsonify(bike_dict), 200
            
#     return jsonify(f"ID not found: bike with id: {verified_id} not found"), 404
            
    
# NEW ROUTES THAT USE SQLALCHEMY AND CONNECT TO THE DB

@bike_bp.route("", methods = ["POST"])
def add_bike():
    # based off of json that comes in the request body
    request_body = request.get_json()

    new_bike = Bike(
        name=request_body["name"],
        price=request_body["price"],
        size=request_body["size"],
        type=request_body["type"],
    )

    # now we want to insert this into our database
    db.session.add(new_bike)
    # DONT FORGET THIS PART:
    db.session.commit()
    # without the commit, bad things happen

    return {"id": new_bike.id}, 201




@bike_bp.route("", methods=["GET"])
def get_all_bikes():
    bikes = Bike.query.all()
    response = []
    for bike in bikes:
        bike_dict = {
            "id": bike.id,
            "name": bike.name,
            "price": bike.price,
            "size": bike.size,
            "type": bike.type
        }
        response.append(bike_dict)

    return jsonify(response), 200