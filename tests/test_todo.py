


def get_auth_token(client):
    client.post("/signup", json={
        "email": "todo@test.com",
        "password": "test123"
    })

    response = client.post("/login", data={
        "username": "todo@test.com",
        "password": "test123"
    })

    return response.json()["access_token"]


def test_create_todo(client):
    token = get_auth_token(client)

    response = client.post(
        "/todos",
        json={
            "title": "Test Todo",
            "description": "Test Desc",
            "completed": False
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Test Todo"


def test_get_todos(client):
    token = get_auth_token(client)

    response = client.get(
        "/todos",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_update_todo(client):
    token = get_auth_token(client)

    
    create_res = client.post(
        "/todos",
        json={"title": "Old", "description": "Old desc"},
        headers={"Authorization": f"Bearer {token}"}
    )

    todo_id = create_res.json()["id"]

    
    response = client.patch(
        f"/todos/{todo_id}",
        json={"title": "Updated"},
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Updated"


def test_delete_todo(client):
    token = get_auth_token(client)

    
    create_res = client.post(
        "/todos",
        json={"title": "Delete Me"},
        headers={"Authorization": f"Bearer {token}"}
    )

    todo_id = create_res.json()["id"]

    
    response = client.delete(
        f"/todos/{todo_id}",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Deleted Successfully"