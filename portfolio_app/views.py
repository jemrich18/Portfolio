from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

# Live, deployed projects — shown on the homepage and full grid on /projects/
PROJECTS = [
    {
        'title': 'Erin the Estie',
        'description': 'A full-stack booking platform built for a real paying client — an esthetician who needed scheduling without a subscription fee. Custom appointment system with an approval workflow, service menu management, and a mobile-optimized admin dashboard. Requirements through deployment, owned end to end.',
        'tech': ['Django', 'PostgreSQL', 'Gmail SMTP', 'Railway'],
        'highlight': 'STATUS: LIVE — PAYING CLIENT · ROLE: Solo build, full SDLC',
        'live_url': 'https://www.erintheestie.com',
        'github_url': '',  # private client repo — leave blank, template hides the button
        'image': 'portfolio_app/images/estie.jpg',
        'has_image': True,
        'icon': 'bi-calendar-check-fill',
        'flagship': True,
    },
    {
        'title': 'FAA Aviation Incident Analysis Dashboard',
        'description': '25 years of NTSB aviation incident data (39,000+ records) explored through an interactive Streamlit dashboard — trend lines, injury-level breakdowns, weather-condition analysis, and a US choropleth heatmap of incident density. Built with the domain expertise of an FAA-certified Airframe Mechanic: every insight is grounded in real aerospace maintenance and regulatory experience, not just the raw numbers.',
        'tech': ['Python', 'Pandas', 'Streamlit', 'Plotly', 'SQLAlchemy'],
        'highlight': 'STATUS: LIVE · DATA: 39,560 NTSB incident records, 2000–present · EDGE: FAA A&P domain expertise',
        'live_url': 'https://faa-aviation-dashboard-ceua43sscr4dsjxyvisprs.streamlit.app/',
        'github_url': 'https://github.com/jemrich18/faa-aviation-dashboard',
        'image': 'portfolio_app/images/faa_dashboard.jpg',
        'has_image': True,
        'icon': 'bi-airplane-engines-fill',
        'flagship': True,
    },
    {
        'title': 'TrackMyHandicap',
        'description': 'A Django REST Framework API implementing the full WHS golf handicap formula from user-submitted rounds — a free alternative to a $60/year official subscription. JWT-authenticated, with a separate React/TypeScript frontend and Stripe integrated for a planned premium tier with extended trend analysis by course and weather condition.',
        'tech': ['Django REST Framework', 'React', 'TypeScript', 'Stripe'],
        'highlight': 'STATUS: LIVE · AUTH: JWT · BILLING: Stripe integrated, premium tier planned',
        'live_url': 'https://trackmyhandi.com',
        'github_url': 'https://github.com/jemrich18/trackmyhandi',
        'image': 'portfolio_app/images/trackmyhandi.jpg',
        'has_image': True,
        'icon': 'bi-flag-fill',
        'flagship': True,
    },
    {
        'title': 'OurCushion',
        'description': 'A real-time shared household finance tracker built around instant accountability — no bank linking, just an honest running balance based on what\u2019s actually logged. Expense and balance updates push instantly to both partners via Django Channels and Redis, with graceful degradation built in: if a WebSocket connection can\u2019t reach Redis, the app still works fully on standard page loads.',
        'tech': ['Django', 'Django Channels', 'WebSockets', 'Redis', 'PostgreSQL'],
        'highlight': 'STATUS: LIVE · REAL-TIME: Channels + Redis, graceful degradation on connection drop',
        'live_url': 'https://ourcushion.com',
        'github_url': 'https://github.com/jemrich18/household_budget',
        'image': 'portfolio_app/images/ourcushion.jpg',
        'has_image': True,
        'icon': 'bi-house-heart-fill',
        'flagship': True,
    },
    {
        'title': 'GolfBros',
        'description': 'A full-stack golf community platform where golfers share round recaps, course conditions, and scores. Users log rounds, report live course conditions to help others plan visits, and browse a community feed — with object-level permissions ensuring users can only edit or delete their own posts.',
        'tech': ['Django REST Framework', 'React', 'Vite', 'PostgreSQL'],
        'highlight': 'STATUS: LIVE · AUTH: DRF token auth · PERMISSIONS: Object-level, owner-only edit/delete',
        'live_url': 'https://www.golfbros.org',
        'github_url': 'https://github.com/jemrich18/Golf_bros_app',
        'image': 'portfolio_app/images/golfbros.jpg',
        'has_image': True,
        'icon': 'bi-golf',
    },
    {
        'title': 'WeatherRack',
        'description': 'A Django app that scores 10-day weather forecasts for deer hunters, ranking each day 0–105 based on five weighted factors (temperature, barometric pressure, wind speed/direction, precipitation, and moon timing) known to drive deer movement. Pulls live forecast data from Open-Meteo and calculates moonrise/moonset astronomically with ephem — no paid APIs required.',
        'tech': ['Django', 'Open-Meteo API', 'ephem', 'PostgreSQL'],
        'highlight': 'STATUS: LIVE · ALGORITHM: 5-factor weighted hunt-day scoring (0–105) · DATA: Free weather + astronomical APIs',
        'live_url': 'https://theweatherrack.com',
        'github_url': 'https://github.com/jemrich18/weather-rack',
        'image': 'portfolio_app/images/weatherrack.jpg',
        'has_image': True,
        'icon': 'bi-cloud-sun-fill',
    },
    {
        'title': 'Budget App',
        'description': 'A full-stack budgeting app for tracking income and expenses, categorizing transactions, and visualizing spending by category. Includes summary cards, date-range filtering, and a Recharts breakdown of expenses by category — with a public read-only demo account so anyone can explore it without registering.',
        'tech': ['Django REST Framework', 'React', 'Recharts', 'Tailwind CSS'],
        'highlight': 'STATUS: LIVE · DEMO: Public read-only demo account available · CHARTS: Recharts spending breakdown',
        'live_url': 'https://budgetappreactdrf-production.up.railway.app',
        'github_url': 'https://github.com/jemrich18/budget_app_react_drf',
        'image': 'portfolio_app/images/budgetapp.jpg',
        'has_image': True,
        'icon': 'bi-cash-coin',
    },
    {
        'title': 'Fit For My Role',
        'description': 'A retrieval-augmented generation pipeline: resumes are parsed with pdfplumber, chunked, and embedded into a ChromaDB vector store. The most relevant chunks are retrieved by similarity search against a job description to ground GPT-4o-mini\u2019s skill-match scoring and generated cover letter in the candidate\u2019s real experience — not general knowledge.',
        'tech': ['Django', 'OpenAI API', 'ChromaDB', 'pdfplumber'],
        'highlight': 'STATUS: LIVE · PIPELINE: pdfplumber \u2192 embeddings \u2192 ChromaDB \u2192 retrieval \u2192 GPT-4o-mini',
        'live_url': 'https://www.fitformyrole.com',
        'github_url': 'https://github.com/jemrich18/rag_application_assistant',
        'image': 'portfolio_app/images/rag.jpg',
        'has_image': True,
        'icon': 'bi-file-earmark-person-fill',
    },
    {
        'title': 'Archery Answers',
        'description': 'A bowhunting ballistics and arrow-building platform: real-world arrow speed estimates from bow specs, kinetic energy and momentum calculators, ethical-harvest threshold ratings by game animal, and a community-submitted arrow component database that powers a full arrow builder with automatic weight/speed/KE calculations.',
        'tech': ['Django', 'HTMX', 'PostgreSQL', 'SQLite'],
        'highlight': 'STATUS: LIVE · CALCULATORS: Arrow speed, KE/momentum, ethical-harvest thresholds · Community component database',
        'live_url': 'https://archeryanswers-production.up.railway.app',
        'github_url': 'https://github.com/jemrich18/Archery_answers',
        'image': 'portfolio_app/images/archery.jpg',
        'has_image': False,
        'icon': 'bi-bullseye',
    },
    {
        'title': 'AI Hunting Chat',
        'description': 'A production-style AI agent built with LangGraph and Django REST Framework. Plain-English requests hit a REST endpoint, and the agent automatically selects the right tool (live weather, calculation, or an internal knowledge base), executes it, and responds in natural language — with full conversation memory across turns via session ID.',
        'tech': ['LangGraph', 'LangChain', 'OpenAI GPT-4o-mini', 'Django REST Framework'],
        'highlight': 'STATUS: LIVE · AGENT: LangGraph tool-routing with cross-turn conversation memory',
        'live_url': 'https://www.aihuntingchat.com',
        'github_url': 'https://github.com/jemrich18/Ai_agent',
        'image': 'portfolio_app/images/ai_agent.jpg',
        'has_image': True,
        'icon': 'bi-robot',
    },
    {
        'title': 'Personal Finance Analysis Dashboard',
        'description': 'An end-to-end data analytics pipeline exploring 1,500 personal finance transactions across 5 years (2020\u20132024): synthetic data generation, data cleaning, SQL-based analysis in SQLite, interactive Plotly visualizations, and a 6-month linear regression forecast. Full workflow documented across 4 Jupyter notebooks covering cleaning, SQL queries, visualization, and forecasting, with dynamic KPI filtering and income/expense breakdowns by category and day of week.',
        'tech': ['Python', 'Pandas', 'SQL', 'Streamlit', 'Plotly', 'Scikit-learn'],
        'highlight': 'STATUS: LIVE · PIPELINE: Synthetic data \u2192 cleaning \u2192 SQL analysis \u2192 visualization \u2192 forecasting',
        'live_url': 'https://end-to-end-finance-data-analysis-4qjvmptdvwcv5mcrfkydze.streamlit.app/',
        'github_url': '',
        'image': 'portfolio_app/images/personalfinance.jpg',
        'has_image': True,
        'icon': 'bi-graph-up-arrow',
    },
]

# In-development projects — not yet publicly deployed. Shown in a separate
# section so the site never claims something is live that isn't.
PROJECTS_IN_PROGRESS = []

SKILLS = {
    'Backend': ['Django', 'Django REST Framework', 'Python', 'Django Channels', 'WebSockets', 'Redis', 'REST API Design'],
    'Data & Analysis': ['Pandas', 'NumPy', 'Streamlit', 'Plotly', 'Recharts', 'Statistical Analysis', 'Data Visualization', 'Scikit-learn'],
    'Frontend': ['React', 'JavaScript', 'TypeScript', 'HTML', 'CSS'],
    'Database': ['PostgreSQL', 'SQLite', 'SQL'],
    'Tools & DevOps': ['Railway', 'Docker', 'Git', 'GitHub Actions', 'CI/CD', 'pytest', 'Jupyter Notebook'],
    'AI / LLM': ['OpenAI API', 'LangGraph', 'ChromaDB', 'RAG Pipelines', 'Vector Embeddings', 'Prompt Engineering'],
}

EDUCATION = [
    {
        'degree': 'B.S. Computer Science — In Progress',
        'school': 'University of Maryland Global Campus',
        'details': 'Algorithms, Data Structures, Databases, Software Engineering',
    },
    {
        'degree': 'Associate of Applied Science',
        'school': 'WSU Tech',
        'details': 'FAA Certified A&P Mechanic',
    },
]


def home(request):
    featured = [p for p in PROJECTS if p.get('flagship')]
    return render(request, 'portfolio_app/home.html', {
        'projects': featured,
        'skills': SKILLS,
        'live_count': len(PROJECTS),
    })


def projects(request):
    return render(request, 'portfolio_app/projects.html', {
        'projects': PROJECTS,
        'projects_in_progress': PROJECTS_IN_PROGRESS,
    })


def about(request):
    return render(request, 'portfolio_app/about.html', {
        'skills': SKILLS,
        'education': EDUCATION,
    })


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        body = request.POST.get('body')
        if name and email and subject and body:
            if not settings.CONTACT_EMAIL:
                messages.error(request, 'Contact form is not configured. Please try again later.')
                return render(request, 'portfolio_app/contact.html')
            try:
                send_mail(
                    subject=f'Portfolio Contact: {subject}',
                    message=f'From: {name}\nEmail: {email}\n\nMessage:\n{body}',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=False,
                )
                messages.success(request, 'Message sent! I will get back to you soon.')
                return redirect('contact')
            except Exception:
                messages.error(request, 'Failed to send message. Please try again later.')
        else:
            messages.error(request, 'Please fill in all fields.')
    return render(request, 'portfolio_app/contact.html')