# Job Collector Bot

A modular job aggregation pipeline that collects **recent job postings**
across:
- 🇺🇸 US Remote roles
- 🇨🇦 Canada (remote, hybrid, in-person)
- Government of Canada
- Universities
- Nonprofit organizations

## Features
- Modular source adapters per job site
- Normalized job schema
- De-duplication across sources
- Country & work-mode classification
- SQLite storage
- Designed for automation & alerts

## Tech Stack
- Python
- HTTPX
- BeautifulSoup
- SQLite
- Playwright (for JS-rendered sites)

## Status
🚧 In progress — currently building core pipeline and first data sources
