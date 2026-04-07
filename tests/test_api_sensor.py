def test_sensor_data_no_api_key(client, mock_firestore):
    response = client.post("/api/sensor_data", json={"temperature": 23.5})

    assert response.status_code == 401
    assert response.get_json() == {"error": "Missing X-API-Key header"}
    mock_firestore["doc_ref"].set.assert_not_called()


def test_sensor_data_wrong_key(client, mock_firestore):
    response = client.post(
        "/api/sensor_data",
        headers={"X-API-Key": "wrong-key"},
        json={"temperature": 23.5},
    )

    assert response.status_code == 401
    assert response.get_json() == {"error": "Unauthorized"}
    mock_firestore["doc_ref"].set.assert_not_called()


def test_sensor_data_valid_key(client, mock_firestore):
    payload = {"temperature": 23.5, "humidity": 41}

    response = client.post(
        "/api/sensor_data",
        headers={"X-API-Key": "test-sensor-key"},
        json=payload,
    )

    assert response.status_code == 201
    body = response.get_json()
    assert body["message"] == "Sensor data received successfully"
    assert body["id"].isdigit()

    mock_firestore["db"].collection.assert_called_with("sensor_data")
    saved_payload = mock_firestore["doc_ref"].set.call_args.args[0]
    assert saved_payload["data"] == payload
    assert "timestamp" in saved_payload