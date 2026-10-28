import pandas as pd
from fastapi import APIRouter, File, HTTPException, UploadFile, status
from io import BytesIO

router = APIRouter(prefix="/reviews", tags=["Reviews"])

REQUIRED_COLUMNS = ["review", "rating"]


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
        df = pd.read_csv(BytesIO(content))
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

    return {
        "status": "valid",
        "filename": filename,
        "total_reviews": len(df),
        "columns": df.columns.tolist(),
    }