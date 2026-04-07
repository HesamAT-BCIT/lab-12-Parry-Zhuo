def test_get_profile_no_auth(client):
    response = client.get("/api/profile")

    assert response.status_code == 401
    assert response.get_json() == {"error": "Missing Authorization header"}


def test_get_profile_bad_token_format(client, mock_firebase_auth):
    response = client.get("/api/profile", headers={"Authorization": "Token invalid"})

    assert response.status_code == 401
    assert response.get_json() == {"error": "Invalid Authorization header format"}
    mock_firebase_auth.assert_not_called()


def test_get_profile_invalid_token(client, mock_firebase_auth, auth_headers):
    mock_firebase_auth.side_effect = Exception("invalid token")

    response = client.get("/api/profile", headers=auth_headers)

    assert response.status_code == 401
    assert response.get_json() == {"error": "Invalid or expired token"}


def test_get_profile_success(client, mock_firestore, mock_firebase_auth, auth_headers):
    mock_firestore["snapshot"].to_dict.return_value = {
        "first_name": "Test",
        "last_name": "User",
        "student_id": "12345678",
    }

    response = client.get("/api/profile", headers=auth_headers)

    assert response.status_code == 200
    assert response.get_json() == {
        "uid": "test_user_123",
        "profile": {
            "first_name": "Test",
            "last_name": "User",
            "student_id": "12345678",
        },
    }
    mock_firebase_auth.assert_called_once_with("valid-test-token")
    mock_firestore["db"].collection.assert_called_with("profiles")
    mock_firestore["collection"].document.assert_called_with("test_user_123")


def test_create_profile_missing_fields(client, mock_firestore, mock_firebase_auth, auth_headers):
    response = client.post(
        "/api/profile",
        headers=auth_headers,
        json={"first_name": "Alice", "last_name": "Smith"},
    )

    assert response.status_code == 400
    assert response.get_json() == {"error": "All fields are required."}
    mock_firebase_auth.assert_called_once_with("valid-test-token")
    mock_firestore["doc_ref"].set.assert_not_called()


def test_create_profile_success(client, mock_firestore, mock_firebase_auth, auth_headers):
    payload = {
        "first_name": "  Alice  ",
        "last_name": "  Smith ",
        "student_id": 12345678,
    }

    response = client.post("/api/profile", headers=auth_headers, json=payload)

    assert response.status_code == 200
    assert response.get_json() == {
        "message": "Profile saved successfully",
        "profile": {
            "first_name": "Alice",
            "last_name": "Smith",
            "student_id": "12345678",
        },
    }
    mock_firebase_auth.assert_called_once_with("valid-test-token")
    mock_firestore["doc_ref"].set.assert_called_once_with(
        {
            "first_name": "Alice",
            "last_name": "Smith",
            "student_id": "12345678",
        },
        merge=False,
    )


def test_update_profile_invalid_field(client, mock_firestore, mock_firebase_auth, auth_headers):
    response = client.put("/api/profile", headers=auth_headers, json={"age": 25})

    assert response.status_code == 400
    assert response.get_json() == {
        "errors": [
            "Invalid field(s): age. Only first_name, last_name, and student_id are allowed."
        ]
    }
    mock_firebase_auth.assert_called_once_with("valid-test-token")
    mock_firestore["doc_ref"].set.assert_not_called()