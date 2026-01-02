from jobbot.core.storage import init_db, upsert_jobs
from jobbot.sources.sample_source import fetch_sample_jobs


def main():
    conn = init_db()

    jobs = fetch_sample_jobs()
    inserted, skipped = upsert_jobs(conn, jobs)

    print(f"Inserted: {inserted} | Skipped (duplicates): {skipped}")


if __name__ == "__main__":
    main()
