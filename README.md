# Jeremiah Emrich — Developer Portfolio

A clean, professional developer portfolio built with Django showcasing my projects, skills, and background as a full-stack developer.

🌐 **Live Site:** [jemrich.dev](https://jemrich.dev)
📄 **Resume:** Available via the live site

---

## About

This portfolio was built from scratch to showcase my work as a Django and full-stack developer. It's intentionally simple and fast — no database required for content, everything is hardcoded for reliability and easy maintenance.

I'm a CS student at the University of Maryland Global Campus, self-taught through Codecademy, and actively freelancing on Fiverr and Upwork.

---

## Featured Projects

| Project | Tech Stack | Live |
|---------|-----------|------|
| WeatherRack | Django, Python, Railway | [weatherrack.com](https://www.weatherrack.com) |
| Archery Answers | Django, PostgreSQL, Railway | [archeryanswers-production.up.railway.app](https://archeryanswers-production.up.railway.app) |
| GolfBros | Django REST Framework, React, PostgreSQL | [golfbros.org](https://www.golfbros.org) |

---

## Tech Stack

**Backend**
- Python 3.12
- Django 6
- Gunicorn

**Frontend**
- HTML5
- Bootstrap 5
- Bootstrap Icons

**Infrastructure**
- Railway (hosting)
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