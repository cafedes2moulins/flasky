from flask import Blueprint
from flask import jsonify

class Bike:
    def __init__(self, id, name, price, size, type):
        self.id = id
        self.name = name
        self.price = price
        self.size = size
        self.type = type


# for now we are going to hardcode some bike data into a list
bikes = [
    Bike(5, "Nina", 100, 48, "gravel"),
    Bike(8, "Bike 3000", 1000, 50, "hybrid"),
    Bike(2, "Auberon", 2000, 55, "electric")
]


bike_bp = Blueprint("bike_bp", __name__, url_prefix="/bike")



# when a request comes in for this prefix, this is the response that I want you to use
# empty "", or an addition to the route -->  "/features"
# and a list for what methods that we want this response to be used for 
@bike_bp.route("", methods=["GET"])
def get_all_bikes():
    #this returns the JSON that will actually be returned to the client

    # we need to convert our python class into json
    #first we must convert to a dictionary, then jsonify can turn it into JSON
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

    # have to jsonify the return
    # response body followed by the status code
    return jsonify(response), 200
    # whatever gets returned here is the response the the request determined 
    # above in the decorator and blueprint

# angular brackets indicate a parameter that a user has to specify
@bike_bp.route("/<bike_id>", methods = ["GET"])
def get_specific_bike(bike_id):
    try:
        verified_id = int(bike_id)
    except ValueError:
        return jsonify("Invalid ID: id must be an integer"), 400

    for bike in bikes:
        if bike.id == verified_id:
            bike_dict = {
                "id": bike.id,
                "name": bike.name,
                "price": bike.price,
                "size": bike.size,
                "type": bike.type
            }
            return jsonify(bike_dict), 200
            
    return jsonify(f"ID not found: bike with id: {verified_id} not found"), 404
            
    
