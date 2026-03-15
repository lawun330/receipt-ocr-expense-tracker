from fastapi import FastAPI

from models import OCRTextRequest, ExpenseRecord
from services.translation_service import translate_text
from services.parsing_service import parse_expense_text
from services.sheets_service import append_expense_record


app = FastAPI(title="ScanSpend Backend", version="0.1.0")


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok"}


@app.post("/parse-expense", response_model=ExpenseRecord)
def parse_expense(payload: OCRTextRequest) -> ExpenseRecord:
    translated_text = translate_text(
        text=payload.text,
        source_lang=payload.language or "th",
        target_lang="en",
    )

    record = parse_expense_text(
        original_text=payload.text,
        translated_text=translated_text,
        source=payload.source,
    )

    append_expense_record(record)
    return record

