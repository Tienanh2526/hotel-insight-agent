import pandas as pd
import pytest

from src.tools.review_statistics import get_review_statistics


def test_calculates_rating_statistics():
    df = pd.DataFrame({
        "review": ["Good", "Great", "Average", "Unknown"],
        "rating": [5, 4, 3, "abc"],
    })

    result = get_review_statistics(df)

    assert result["total_reviews"] == 4
    assert result["valid_rating_count"] == 3
    assert result["invalid_rating_count"] == 1
    assert result["average_rating"] == 4.0


def test_missing_rating_column():
    df = pd.DataFrame({"review": ["Good"]})

    with pytest.raises(ValueError):
        get_review_statistics(df)