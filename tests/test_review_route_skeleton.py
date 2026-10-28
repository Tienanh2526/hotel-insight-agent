from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_validate_endpoint_rejects_non_csv() -> None:
    response = client.post(
        "/api/v1/reviews/validate",
        files={"file": ("reviews.txt", b"not a csv", "text/plain")},
    )
    assert response.status_code == 415
