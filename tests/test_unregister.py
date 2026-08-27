def test_unregister_removes_participant(client):
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"  # already seeded participant

    # Act
    response = client.delete(f"/activities/{activity_name}/unregister", params={"email": email})

    # Assert
    assert response.status_code == 200
    activities = client.get("/activities").json()
    assert email not in activities[activity_name]["participants"]


def test_unregister_not_signed_up_returns_400(client):
    # Arrange
    activity_name = "Chess Club"
    email = "not-signed-up@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity_name}/unregister", params={"email": email})

    # Assert
    assert response.status_code == 400
    assert "not signed up" in response.json()["detail"]


def test_unregister_unknown_activity_returns_404(client):
    # Arrange
    activity_name = "Nonexistent Activity"
    email = "student@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity_name}/unregister", params={"email": email})

    # Assert
    assert response.status_code == 404
