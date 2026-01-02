from jobbot.core.models import Job


def fetch_sample_jobs() -> list[Job]:
    return [
        Job(
            source="sample",
            source_id="001",
            title="Junior Data Analyst",
            company="Example University",
            url="https://example.com/jobs/001",
            location_text="Waterloo, ON (Hybrid)",
            category="university",
            snippet="Work with dashboards, reporting, and basic analytics.",
            date_posted="2026-01-01",
        ),
        Job(
            source="sample",
            source_id="002",
            title="Software Developer Intern",
            company="Nonprofit Org",
            url="https://example.com/jobs/002",
            location_text="Remote (Canada)",
            category="nonprofit",
            snippet="Build internal tools and automate workflows.",
            date_posted="2026-01-02",
        ),
    ]
