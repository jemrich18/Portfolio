# Jeremiah Emrich — Backend Software Engineer (Python / Django)

A clean, fast developer portfolio built with Django showcasing my projects, skills, and background as a backend developer.

🌐 **Live Site:** [jemrich.dev](https://jemrich.dev)
📄 **Resume:** Available via the live site

---

## About

Self-taught backend developer specializing in Python and Django, with 10 deployed production applications. Core strength in Django REST Framework, PostgreSQL, and real-time backend architecture using Django Channels, WebSockets, and Redis. Delivered a live client booking platform end-to-end and shipped production AI/LLM integrations — a RAG pipeline and a LangGraph tool-calling agent — as an additional area of depth.

Currently a CS student at the University of Maryland Global Campus. FAA-certified Airframe mechanic background adds discipline in safety-critical systems and precision documentation — put directly to use in the FAA Aviation Incident Analysis Dashboard below.

This portfolio was built from scratch to showcase that work. It's intentionally simple and fast — no database required for content, everything is hardcoded for reliability and easy maintenance.

---

## Featured Projects

| Project | Tech Stack | Live |
|---|---|---|
| Erin the Estie | Django, PostgreSQL, Railway | [erintheestie.com](https://erintheestie.com) |
| FAA Aviation Incident Dashboard | Python, Pandas, Plotly, Streamlit | [Live Demo](https://faa-aviation-dashboard-ceua43sscr4dsjxyvisprs.streamlit.app/) |
| TrackMyHandicap | Django REST Framework, React, PostgreSQL, Stripe | [trackmyhandi.com](https://trackmyhandi.com) |
| OurCushion | Django, Channels, WebSockets, Redis, PostgreSQL | [ourcushion.com](https://ourcushion.com) |
| GolfBros | Django REST Framework, React, Vite, PostgreSQL | [golfbros.org](https://www.golfbros.org) |
| WeatherRack | Django, Python, Open-Meteo, ephem, Railway | [theweatherrack.com](https://theweatherrack.com) |
| Budget App | Django REST Framework, React, Recharts, Tailwind | [Live Demo](https://budgetappreactdrf-production.up.railway.app) |
| Fit For My Role (AI) | Django, OpenAI API, ChromaDB, pdfplumber | [fitformyrole.com](https://fitformyrole.com) |
| Archery Answers | Django, HTMX, PostgreSQL | [Live Demo](https://archeryanswers-production.up.railway.app) |
| AI Hunting Chat | LangGraph, LangChain, OpenAI, Django REST Framework | [aihuntingchat.com](https://www.aihuntingchat.com) |

---

## Tech Stack

**Backend**
- Python 3.12
- Django 6
- Django REST Framework
- Django Channels / WebSockets / Redis
- Gunicorn

**Frontend**
- React, TypeScript, JavaScript
- HTML5
- Bootstrap 5
- Bootstrap Icons

**AI / LLM**
- OpenAI API (GPT-4o-mini)
- LangChain / LangGraph
- ChromaDB, vector embeddings, RAG pipelines

**Infrastructure**
- Railway (hosting)
- PostgreSQL
- Docker
- GitHub Actions (CI/CD)
- Whitenoise (static files)
- Git & GitHub

---

## Features

- Fully hardcoded content — no database needed for projects or skills
- Contact form with Gmail SMTP email notifications
- Downloadable resume
- Deployed on Railway with custom domain
- Mobile responsive via Bootstrap 5

---

## Local Development

### Prerequisites
- Python 3.12+
- uv package manager

### Setup

1. Clone the repo
```bash
git clone https://github.com/jemrich18/portfolio.git
cd portfolio
```

2. Install dependencies
```bash
uv install
```

3. Run the development server
```bash
uv run python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

---

## Deployment

Deployed on [Railway](https://railway.app) with a custom domain at [jemrich.dev](https://jemrich.dev).

**Environment variables required:**