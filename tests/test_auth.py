
def test_signup(client):
    response = client.post("/signup", json={
        "email": "test@example.com",
        "password": "test123"
    })
    assert response.status_code in [200, 400]  



def test_login(client):
    response = client.post("/login", data={
        "username": "test@example.com",
        "password": "test123"
    })
    assert response.status_code in [200, 401, 400]
