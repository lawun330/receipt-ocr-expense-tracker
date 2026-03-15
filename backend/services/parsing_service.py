import re
from datetime import date
from typing import Optional

from models import ExpenseItem, ExpenseRecord


def _extract_total_amount(text: str) -> Optional[float]:
    number_pattern = re.compile(r"(\d+[.,]\d{2})")
    candidates = [m.group(1).replace(",", "") for m in number_pattern.finditer(text)]
    if not candidates:
        return None
    try:
        return float(candidates[-1])
    except ValueError:
        return None


def _extract_merchant(text: str) -> Optional[str]:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return None
    return lines[0][:100]


def _normalize_items(translated_text: str) -> list[ExpenseItem]:
    items: list[ExpenseItem] = []
    for raw_line in translated_text.splitlines():
        line = raw_line.strip()
        if not line:
            continue

        lower = line.lower()
        normalized_name = line
        category: Optional[str] = None

        if "meow" in lower or "cat" in lower:
            normalized_name = "cat food"
            category = "pet"

        item = ExpenseItem(
            original_name=line,
            normalized_name=normalized_name,
            category=category,
        )
        items.append(item)

    return items


def parse_expense_text(
    original_text: str,
    translated_text: str,
    source: Optional[str] = None,
) -> ExpenseRecord:
    total_amount = _extract_total_amount(translated_text or original_text)
    merchant = _extract_merchant(translated_text or original_text)
    items = _normalize_items(translated_text or original_text)

    record = ExpenseRecord(
        date=date.today(),
        merchant=merchant,
        total_amount=total_amount,
        main_category=None,
        items=items,
        raw_text=original_text,
        translated_text=translated_text or None,
        source=source,
    )

    return record

