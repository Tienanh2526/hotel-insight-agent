from pathlib import Path

from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

SAMPLE_CSV = Path("data/raw/sample_reviews_synthetic.csv")


def post_csv(content: bytes, filename: str = "reviews.csv"):
    return client.post(
        "/api/v1/reviews/validate",
        files={"file": (filename, content, "text/csv")},
    )


def test_validate_endpoint_rejects_non_csv() -> None:
    response = client.post(
        "/api/v1/reviews/validate",
        files={"file": ("reviews.txt", b"not a csv", "text/plain")},
    )
    assert response.status_code == 415


def test_validate_accepts_sample_file() -> None:
    response = post_csv(SAMPLE_CSV.read_bytes(), SAMPLE_CSV.name)

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "valid"
    assert body["total_reviews"] > 0
    assert "review_id" in body["columns"]


def test_validate_rejects_missing_required_columns() -> None:
    response = post_csv(b"review,rating\nGreat room,5\n")

    assert response.status_code == 400
    assert response.json()["detail"]["missing_columns"] == ["review_id", "review_text"]


def test_rating_column_is_optional() -> None:
    response = post_csv(b"review_id,review_text\nr1,Clean room\n")

    assert response.status_code == 200
    assert response.json()["status"] == "valid"


def test_validate_flags_blank_values_and_duplicate_ids() -> None:
    csv = (
        b"review_id,review_text\n"
        b"r1,Clean room\n"
        b"r1,Noisy at night\n"
        b",Friendly staff\n"
        b"r3,   \n"
    )
    response = post_csv(csv)

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "has_issues"
    assert body["issues"] == {
        "blank_review_id_rows": [4],
        "blank_review_text_rows": [5],
        "duplicate_review_ids": ["r1"],
    }
