import sqlite3
from pathlib import Path
from typing import Iterable, Tuple

from jobbot.core.models import Job


def init_db(db_path: str = "jobbot/data/jobs.db") -> sqlite3.Connection:
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)

    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS jobs (
            pk TEXT PRIMARY KEY,
            source TEXT NOT NULL,
            source_id TEXT NOT NULL,
            title TEXT NOT NULL,
            company TEXT NOT NULL,
            url TEXT NOT NULL,
            location_text TEXT,
            country TEXT,
            work_mode TEXT,
            category TEXT,
            date_posted TEXT,
            date_seen TEXT NOT NULL,
            snippet TEXT
        )
        """
    )
    conn.commit()
    return conn


def job_pk(job: Job) -> str:
    # unique per source posting
    return f"{job.source}:{job.source_id}"


def upsert_jobs(conn: sqlite3.Connection, jobs: Iterable[Job]) -> Tuple[int, int]:
    inserted, skipped = 0, 0

    for job in jobs:
        try:
            conn.execute(
                """
                INSERT INTO jobs VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
                """,
                (
                    job_pk(job),
                    job.source,
                    job.source_id,
                    job.title,
                    job.company,
                    job.url,
                    job.location_text,
                    job.country,
                    job.work_mode,
                    job.category,
                    job.date_posted,
                    job.date_seen,
                    job.snippet,
                ),
            )
            inserted += 1
        except sqlite3.IntegrityError:
            skipped += 1

    conn.commit()
    return inserted, skipped
