from fastapi.testclient import TestClient

from src.app import app, activities


client = TestClient(app)


def test_unregister_participant_from_activity():
    activity_name = "Chess Club"
    participant_email = "michael@mergington.edu"

    response = client.delete(f"/activities/{activity_name}/participants/{participant_email}")

    assert response.status_code == 200
    assert participant_email not in activities[activity_name]["participants"]
    assert response.json()["message"] == f"Removed {participant_email} from {activity_name}"


def test_activities_endpoint_disables_caching():
    response = client.get("/activities")

    assert response.status_code == 200
    assert response.headers["cache-control"].lower() == "no-store"
