import pandas as pd


def get_review_statistics(df: pd.DataFrame) -> dict:
    """Calculate basic statistics for hotel reviews."""

    if "rating" not in df.columns:
        raise ValueError("Missing required column: rating")

    ratings = pd.to_numeric(df["rating"], errors="coerce")
    valid_ratings = ratings.dropna()

    distribution = {
        str(int(rating)): int(count)
        for rating, count in valid_ratings.value_counts().sort_index().items()
    }

    average_rating = (
        round(float(valid_ratings.mean()), 2)
        if not valid_ratings.empty
        else None
    )

    return {
        "total_reviews": len(df),
        "valid_rating_count": int(valid_ratings.count()),
        "invalid_rating_count": int(ratings.isna().sum()),
        "average_rating": average_rating,
        "rating_distribution": distribution,
    }