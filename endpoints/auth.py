from locust import HttpUser

def login(client):
    token_credentials = {
        "username": "admin",
        "password": "password123"
    }
    with client.post("/auth", json = token_credentials, catch_response=True, name="/auth") as response:
        if response.status_code == 200:
            return response.json().get("token")
        else:
            response.failure(f"Auth failed: {response.text}")
            return None