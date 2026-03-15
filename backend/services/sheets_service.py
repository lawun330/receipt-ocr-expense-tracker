from datetime import datetime
from typing import Any, List

from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

from models import ExpenseRecord


SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]


def _get_credentials() -> Credentials:
    """
    load google service account credentials from the path in GOOGLE_APPLICATION_CREDENTIALS.
    """
    import os

    creds_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not creds_path:
        raise RuntimeError("GOOGLE_APPLICATION_CREDENTIALS is not set")

    return Credentials.from_service_account_file(creds_path, scopes=SCOPES)


def _get_sheet_id() -> str:
    """
    read target sheet id from environment variable GOOGLE_SHEET_ID.
    """
    import os

    sheet_id = os.environ.get("GOOGLE_SHEET_ID")
    if not sheet_id:
        raise RuntimeError("GOOGLE_SHEET_ID is not set")
    return sheet_id


def _record_to_row(record: ExpenseRecord) -> List[Any]:
    items_summary = "; ".join(
        f"{item.normalized_name or item.original_name}"
        for item in record.items
        if item.original_name
    )

    return [
        datetime.utcnow().isoformat(),
        record.date.isoformat() if record.date else "",
        record.merchant or "",
        record.total_amount if record.total_amount is not None else "",
        record.currency,
        record.main_category or "",
        items_summary,
        (record.raw_text[:200] + "...") if len(record.raw_text) > 200 else record.raw_text,
        record.source or "",
    ]


def append_expense_record(record: ExpenseRecord) -> None:
    """
    append a single expense record as a new row in the target google sheet.
    """
    creds = _get_credentials()
    service = build("sheets", "v4", credentials=creds)

    sheet_id = _get_sheet_id()
    body = {"values": [_record_to_row(record)]}

    service.spreadsheets().values().append(
        spreadsheetId=sheet_id,
        range="Sheet1!A1",
        valueInputOption="USER_ENTERED",
        insertDataOption="INSERT_ROWS",
        body=body,
    ).execute()

