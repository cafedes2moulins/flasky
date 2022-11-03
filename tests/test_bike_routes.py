def test_get_all_bikes_with_empty_db_returns_empty_list(client):
    response = client.get("/bike")
    # sends GET request
    response_body = response.get_json()
    # gets json response

    # now we are going to run assertions
    assert response.status_code == 200
    assert response_body == []


# did not set up GET for one bike route, so this test will fail
def test_get_one_bike_with_empty_db_returns_404(client):
    response = client.get("/bike/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert "message" in response_body
    # checking in json response, similar to chcking for a key in a dictionary
    

# creating a test that prepopulated db values
def test_get_one_bike_with_populated_db_returns_bike_json(client, two_bikes):
    response = client.get("/bike/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Edison",
        "price": 600,
        "size": 43,
        "type": "electric"
    }


def test_post_one_bike_creates_bike_in_db(client, two_bikes):
    response = client.post("/bike", json={
        "name": "New Bike",
        "price": 300,
        "size": 23,
        "type": "childs"
    })
    response_body = response.get_json()

    assert response.status_code == 201
    assert "id" in response_body
    assert response_body["id"] == 3