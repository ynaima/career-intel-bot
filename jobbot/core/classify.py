import re
from jobbot.core.models import Job

CANADA_PROVINCES = r"\b(ON|BC|AB|MB|SK|QC|NS|NB|NL|PE|YT|NT|NU)\b"


def infer_country(location_text: str) -> str | None:
    t = (location_text or "").lower()

    if "canada" in t or re.search(CANADA_PROVINCES, location_text or ""):
        return "CA"
    if "united states" in t or re.search(r"\b(usa|us)\b", t):
        return "US"
    return None


def infer_work_mode(title: str, location_text: str) -> str:
    t = f"{title} {location_text}".lower()

    # order matters
    if "hybrid" in t:
        return "hybrid"
    if "remote" in t or "work from home" in t or "wfh" in t:
        return "remote"
    if location_text.strip():
        return "onsite"
    return "unknown"


def enrich(job: Job) -> Job:
    # country
    if not job.country:
        job.country = infer_country(job.location_text)

    # work mode
    if job.work_mode == "unknown":
        job.work_mode = infer_work_mode(job.title, job.location_text)

    # remote region label
    if job.work_mode == "remote" and job.country == "US":
        job.remote_region = "US-Remote"
    elif job.work_mode == "remote" and job.country == "CA":
        job.remote_region = "Canada-Remote"
    else:
        job.remote_region = None

    return job
