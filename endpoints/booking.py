from locust import HttpUser

def create_booking(client, data):
    with client.post("/booking", json=data, catch_response=True, name="/booking [POST]") as response:
        if response.status_code == 200:
            return response.json().get("bookingid")
        else:
            response.failure(f"Booking creation failed: {response.text}")


def get_booking(client, booking_id):
    with client.get(f"/booking/{booking_id}", catch_response =True, name="/booking/:id [GET]") as response:
        if response.status_code != 200:
            response.failure(f"Get booking failed: {response.text}")

def delete_booking(client, booking_id, token):
    headers = {"Cookie": f"token={token}"}
    with client.delete(f"/booking/{booking_id}", headers=headers, catch_response =True,  name="/booking/:id [DELETE]") as response:
        if response.status_code != 201:
            response.failure(f"Delete booking failed: {response.text}")