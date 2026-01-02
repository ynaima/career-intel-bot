from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Job:
    source: str             
    source_id: str           # stable id from the source
    title: str
    company: str
    url: str

    location_text: str = ""
    country: Optional[str] = None          # "CA" or "US"
    work_mode: str = "unknown"             # "remote" | "hybrid" | "onsite" | "unknown"
    category: Optional[str] = None         # "government" | "university" | "nonprofit" | etc.

    date_posted: Optional[str] = None      # ISO date string if available
    date_seen: str = datetime.utcnow().isoformat(timespec="seconds")
    snippet: str = ""
