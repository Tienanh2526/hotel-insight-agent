from io import BytesIO

import pandas as pd
from fastapi import APIRouter, File, HTTPException, UploadFile, status

router = APIRouter(prefix="/reviews", tags=["Reviews"])

# Theo docs/04_data_spec.md: chỉ 2 cột này bắt buộc, các cột khác (rating, hotel_id...) là tuỳ chọn.
REQUIRED_COLUMNS = ["review_id", "review_text"]


def _blank_rows(series: pd.Series) -> list[int]:
    """Trả về số dòng trong file CSV (dòng 1 là header) có giá trị rỗng."""
    is_blank = series.isna() | (series.astype(str).str.strip() == "")
    return [int(index) + 2 for index in series[is_blank].index]


@router.post("/validate", status_code=status.HTTP_200_OK)
async def validate_reviews_csv(file: UploadFile = File(...)) -> dict:
    filename = file.filename or ""

    if not filename.lower().endswith(".csv"):
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail="Please upload a .csv file.",
        )

    content = await file.read()

    try:
        # utf-8-sig: bỏ ký tự BOM mà Excel hay chèn vào đầu file.
        # dtype=str: giữ nguyên review_id như "001", không để pandas đổi thành số 1.
        df = pd.read_csv(BytesIO(content), encoding="utf-8-sig", dtype=str)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Unable to read CSV file.",
        )

    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "message": "Missing required columns.",
                "missing_columns": missing_columns,
            },
        )

    review_ids = df["review_id"].str.strip()
    duplicate_ids = sorted(
        review_ids[review_ids.duplicated() & review_ids.ne("")].dropna().unique()
    )

    issues = {
        "blank_review_id_rows": _blank_rows(df["review_id"]),
        "blank_review_text_rows": _blank_rows(df["review_text"]),
        "duplicate_review_ids": duplicate_ids,
    }
    has_issues = any(issues.values())

    return {
        "status": "has_issues" if has_issues else "valid",
        "filename": filename,
        "total_reviews": len(df),
        "columns": df.columns.tolist(),
        "issues": issues,
    }
