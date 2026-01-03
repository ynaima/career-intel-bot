from jobbot.core.storage import init_db, upsert_jobs
from jobbot.core.classify import enrich
from jobbot.core.filters import is_recent, matches_targets
from jobbot.sources.sample_source import fetch_sample_jobs


def main():
    conn = init_db()

    jobs = [enrich(j) for j in fetch_sample_jobs()]
    jobs = [j for j in jobs if is_recent(j, days=30) and matches_targets(j)]

    inserted, skipped = upsert_jobs(conn, jobs)
    print(f"Inserted: {inserted} | Skipped (duplicates): {skipped}")

    for j in jobs:
        print(f"- [{j.country} | {j.work_mode}] {j.title} @ {j.company} ({j.location_text})")


if __name__ == "__main__":
    main()
