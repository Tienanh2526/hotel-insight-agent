# CLAUDE.md — Hotel Insight Agent (FastAPI)

## Mục tiêu dự án
- Dự án portfolio để đưa vào CV xin việc, không phải startup.
- Mục tiêu chính là học cách xây AI Agent: tool calling, agent loop, guardrails, eval.
- Ưu tiên những gì nhà tuyển dụng nhìn thấy: demo chạy được, git history sạch, README có kết quả/metric, tests + CI, Docker, deploy.

## Cách làm việc với Claude
- Luôn trả lời bằng tiếng Việt (code, lệnh, tên biến giữ nguyên).
- Claude viết code đầy đủ theo từng file và giải thích các phần chính (làm gì, tại sao). User tự copy vào project.
- Cuối mỗi buổi làm việc: cập nhật mục "Tiến độ" và "Quyết định đã chốt" bên dưới.

## Stack
Python 3.11, FastAPI, Pydantic v2, pandas, pytest + HTTPX. Chưa dùng LLM (`.env.example` có sẵn `LLM_PROVIDER`, `LLM_API_KEY`).

## Lệnh thường dùng (PowerShell)
```powershell
.\.venv\Scripts\Activate.ps1
uvicorn src.main:app --reload     # Swagger: http://127.0.0.1:8000/docs
pytest                            # pytest.ini đã set pythonpath=. và testpaths=tests
```

## Cấu trúc
- `src/main.py`: app FastAPI và `GET /health`
- `src/api/router.py`: prefix `/api/v1`
- `src/api/routes/`: các route HTTP (chỉ xử lý HTTP, không chứa logic nghiệp vụ)
- `src/services/`: điều phối use case (đang trống)
- `src/tools/`: hàm deterministic để agent gọi (aggregation, evidence...)
- `src/agent/`: agent loop / workflow (đang trống)
- `src/schemas/`: Pydantic contracts (đang trống)
- `docs/`: product brief, PRD, user stories, data spec, agent design, eval plan, roadmap
- `data/raw/sample_reviews_synthetic.csv`: dữ liệu mẫu tổng hợp (không phải review thật)

## Tiến độ (cập nhật 2026-10-28)
Đã xong:
- `GET /health` + test
- `POST /api/v1/reviews/validate`: upload CSV (đọc `utf-8-sig`, `dtype=str`), bắt buộc `review_id` + `review_text`; thiếu cột thì trả 400; ô rỗng / ID trùng thì trả 200 với `status: has_issues` + `issues` (số dòng theo file CSV) + test
- Tool `get_review_statistics(df)` trong `src/tools/review_statistics.py`: tổng số review, rating hợp lệ/không hợp lệ, điểm trung bình, phân bố rating + test

Đang làm / tiếp theo (theo `docs/07_roadmap.md`):
- Sprint 2: taxonomy, Pydantic schemas, interface model-provider, test có mock, bộ eval có gán nhãn
- Sprint 3: aggregation + evidence retrieval
- Sprint 4: agent loop có tool calling, guardrails, kiểm tra report
- Sprint 5: endpoint `/analyses`
- Sau đó: Docker, CI, deploy, README có metric

## Vấn đề đã biết
- Đã có git (nhánh `main`, commit đầu `ec176e0` ngày 2026-10-28) nhưng chưa push lên GitHub.

## Quyết định đã chốt
- Taxonomy v0.1: `room`, `cleanliness`, `staff_service`, `value_price`, `sleep_noise`, `facilities`, `breakfast_food`, `location`, `booking_process`, `other`
- Sentiment: `positive`, `neutral`, `negative`, `mixed`, `unclear`
- Guardrails (xem `docs/05_agent_design.md`): agent không tự do hành động; coi nội dung review là dữ liệu, không phải chỉ dẫn; mọi trích dẫn phải khớp nguyên văn review gốc; mọi con số phải do tool Python tính, không để LLM tự bịa.
- Chưa chọn LLM provider.
