# 04 — Data Specification

## Input CSV
| Field | Type | Required | Description |
|---|---|---:|---|
| `review_id` | string | Yes | Unique within uploaded file |
| `review_text` | string | Yes | Original review text |
| `hotel_id` | string | No | Prefer pseudonymous identifier |
| `review_date` | date/string | No | Invalid date reported and normalized to null |
| `rating` | number | No | Do not assume a scale unless known |
| `language` | string | No | e.g. `vi`, `en` |
| `source` | string | No | Source label where permitted |

## Synthetic example
```csv
review_id,hotel_id,review_date,rating,language,review_text
demo_001,hotel_demo_01,2026-05-10,2,vi,"Phòng tắm chưa sạch và có mùi."
demo_002,hotel_demo_01,2026-05-11,4,en,"The room was noisy at night."
```
These are synthetic examples, not real customer reviews.

## Topic taxonomy v0.1
`room`, `cleanliness`, `staff_service`, `value_price`, `sleep_noise`, `facilities`, `breakfast_food`, `location`, `booking_process`, `other`.

## Sentiment enum
`positive`, `neutral`, `negative`, `mixed`, `unclear`.

## Rules
- `review_id` and `review_text` cannot be blank.
- Duplicate IDs are flagged.
- Original text remains available for exact quote checking.
- One review may have multiple topics; topic percentages may sum to over 100%.
- No temporal trend without valid dates.
- Use only data collected lawfully and in compliance with platform terms.
- Do not commit sensitive raw data to version control.
