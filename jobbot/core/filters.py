from datetime import datetime, timedelta
from jobbot.core.models import Job


def is_recent(job: Job, days: int = 14) -> bool:
    """
    Prefer date_posted if present; fallback to date_seen.
    Accepts ISO dates like '2026-01-02' or full ISO timestamps.
    """
    cutoff = datetime.utcnow() - timedelta(days=days)

    for dt_str in [job.date_posted, job.date_seen]:
        if not dt_str:
            continue
        try:
            # allow YYYY-MM-DD
            if len(dt_str) == 10:
                dt = datetime.fromisoformat(dt_str)
            else:
                dt = datetime.fromisoformat(dt_str.replace("Z", ""))
            return dt >= cutoff
        except ValueError:
            continue

    return False


def matches_targets(job: Job) -> bool:
    """
    Your goals:
    - US: remote jobs
    - Canada: remote OR hybrid OR onsite
    - Also tagged categories (government/nonprofit/university) later
    """
    if job.country == "US":
        return job.work_mode == "remote"
    if job.country == "CA":
        return job.work_mode in {"remote", "hybrid", "onsite"}
    return False
