# Jeremiah Emrich — Backend Developer (Python / Django)

A clean, fast developer portfolio built with Django showcasing my projects, skills, and background as a backend developer.

🌐 **Live Site:** [jemrich.dev](https://jemrich.dev)
📄 **Resume:** Available via the live site

---

## About

Self-taught backend developer specializing in Python and Django, with 11 deployed production applications. Core strength in Django REST Framework, PostgreSQL, and real-time backend architecture using Django Channels, WebSockets, and Redis. Delivered a live client booking platform end-to-end and shipped production AI/LLM integrations as an additional area of depth.

Currently a CS student at the University of Maryland Global Campus. FAA-certified Airframe mechanic background adds discipline in safety-critical systems and precision documentation.

This portfolio was built from scratch to showcase that work. It's intentionally simple and fast — no database required for content, everything is hardcoded for reliability and easy maintenance.

---

## Featured Projects

| Project | Tech Stack | Live |
|---|---|---|
| Erin the Estie | Django, PostgreSQL, Railway | [erintheestie.com](https://erintheestie.com) |
| Work Order Tracker *(in progress)* | Django, Channels, WebSockets, Redis, PostgreSQL | — |
| OurCushion *(in progress)* | Django, Channels, WebSockets, PostgreSQL | [ourchushion.com](https://ourchushion.com) |
| Budget App | Django REST Framework, React, PostgreSQL, Railway | — |
| GolfBros | Django REST Framework, React, PostgreSQL | [golfbros.org](https://www.golfbros.org) |
| WeatherRack | Django, Python, Railway | [theweatherrack.com](https://theweatherrack.com) |
| FAA Aviation Incident Dashboard | Python, Pandas, Plotly, Streamlit | — |
| Job Application Assistant (AI) | Django, LangChain, OpenAI, ChromaDB | [fitformyrole.com](https://fitformyrole.com) |
| Hunting AI Assistant (AI Agent) | Django, LangGraph, LangChain, OpenAI | — |
| Archery Answers | Django, PostgreSQL, Railway | [archeryanswers-production.up.railway.app](https://archeryanswers-production.up.railway.app) |

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