def test_get_activities_returns_seeded_data(client):
    # Arrange
    # (activities are seeded by src.app on import)

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data


def test_get_activities_entries_have_expected_fields(client):
    # Arrange
    # (activities are seeded by src.app on import)

    # Act
    response = client.get("/activities")

    # Assert
    data = response.json()
    for details in data.values():
        assert "description" in details
        assert "schedule" in details
        assert "max_participants" in details
        assert "participants" in details
