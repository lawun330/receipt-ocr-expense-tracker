from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class OCRTextRequest(BaseModel):
    text: str = Field(..., description="Raw OCR text from the mobile app")
    language: str = Field("th", description="Source language code, default Thai")
    source: Optional[str] = Field(
        default=None, description="Optional source identifier (e.g. device or app version)"
    )


class ExpenseItem(BaseModel):
    original_name: str
    normalized_name: str
    quantity: Optional[float] = None
    unit_price: Optional[float] = None
    total_price: Optional[float] = None
    category: Optional[str] = None


class ExpenseRecord(BaseModel):
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Timestamp when this record was created in the backend",
    )
    date: Optional[date] = None
    merchant: Optional[str] = None
    total_amount: Optional[float] = None
    currency: str = "THB"
    main_category: Optional[str] = None
    items: List[ExpenseItem] = Field(default_factory=list)
    raw_text: str
    translated_text: Optional[str] = None
    source: Optional[str] = None

