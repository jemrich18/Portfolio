from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings 

# Create your views here.
PROJECTS = [
    {
        'title': 'Job Application Assistant',
        'description': 'Upload your resume and a job posting — the app scores your match percentage, surfaces your exact skill gaps, and generates a tailored cover letter. Built on a full RAG pipeline: PDF parsing, vector embedding, retrieval, and GPT-4o-mini completion with structured output. A production AI tool built for real use.',
        'tech': ['Django', 'OpenAI', 'LangChain', 'RAG', 'ChromaDB', 'Python', 'Railway'],
        'live_url': 'https://www.fitformyrole.com',
        'github_url': 'https://github.com/jemrich18/rag_application_assistant',
        'category': 'AI / Full Stack',
        'image': 'portfolio_app/images/rag.jpg',
    },
    {
        'title': 'Hunting AI Assistant',
        'description': 'A domain-specific AI agent built with LangGraph and Django. Routes plain-English queries through a multi-node state graph across 10+ topic domains — live weather tools, knowledge base Q&A, and conversation memory. Engineered specifically to prevent hallucination on regulation-sensitive topics.',
        'tech': ['Django', 'LangGraph', 'LangChain', 'OpenAI', 'DRF', 'Railway'],
        'live_url': 'https://www.aihuntingchat.com',
        'github_url': 'https://github.com/jemrich18/Ai_agent',
        'category': 'AI / Full Stack',
        'image': 'portfolio_app/images/ai.jpg',
    },
    {
        'title': 'Erin the Estie',
        'description': 'A full-stack booking platform built for a real paying client. Custom appointment booking system with approval workflow, service menu management, and mobile-optimized admin dashboard. Django backend with Gmail SMTP integration, deployed with a custom domain. Real requirements, real delivery, real maintenance.',
        'tech': ['Django', 'PostgreSQL', 'Gmail SMTP', 'Railway'],
        'live_url': 'https://www.erintheestie.com',
        'github_url': 'https://github.com/jemrich18/erin-the-estie',
        'category': 'Client Project',
        'image': 'portfolio_app/images/estie.jpg',
    },
    {
        'title': 'FAA Aviation Incident Dashboard',
        'description': 'Interactive dashboard analyzing 39,000+ US aviation incidents from the NTSB database. Features dynamic filters, KPI metrics, trend analysis, aircraft make breakdowns, and a US choropleth map. Built by an FAA-certified A&P mechanic — domain expertise that goes beyond the data.',
        'tech': ['Python', 'Pandas', 'Plotly', 'Streamlit', 'NTSB Data'],
        'live_url': 'https://faa-aviation-dashboard-ceua43sscr4dsjxyvisprs.streamlit.app/',
        'github_url': 'https://github.com/jemrich18/faa-aviation-dashboard',
        'category': 'Data Analysis',
        'image': 'portfolio_app/images/faa.jpg',
    },
    {
        'title': 'WeatherRack',
        'description': 'A Django web app that scores 10-day weather forecasts against the variables that actually drive deer movement — wind, pressure, temperature swing, and moon phase. Returns a ranked list of your best hunting days so you stop guessing. Features location management and a responsive dark UI.',
        'tech': ['Django', 'Python', 'PostgreSQL', 'Railway'],
        'live_url': 'https://www.theweatherrack.com',
        'github_url': 'https://github.com/jemrich18/weatherrack',
        'category': 'Full Stack',
        'image': 'portfolio_app/images/weatherrack.jpg',
    },
    {
        'title': 'Budget App',
        'description': 'Full-stack personal finance tracker with a Django REST Framework backend and React frontend. Features token authentication, category management, full CRUD, expense visualization with chart breakdowns, pytest unit tests, and a GitHub Actions CI/CD pipeline.',
        'tech': ['Django REST Framework', 'React', 'PostgreSQL', 'Railway'],
        'live_url': 'https://budgetappreactdrf-production.up.railway.app',
        'github_url': 'https://github.com/jemrich18/budget_app_react_drf',
        'category': 'Full Stack',
        'image': 'portfolio_app/images/budget.jpg',
    },
    {
        'title': 'GolfBros',
        'description': 'A full-stack golf community platform where players log rounds, share course reviews, and track performance over time. Built with Django REST Framework, React, and PostgreSQL. Features user authentication, full CRUD, and a clean responsive UI.',
        'tech': ['Django REST Framework', 'React', 'PostgreSQL', 'Railway'],
        'live_url': 'https://www.golfbros.org',
        'github_url': 'https://github.com/jemrich18/golfbros',
        'category': 'Full Stack',
        'image': 'portfolio_app/images/golfbros.jpg',
    },
    {
        'title': 'Archery Answers',
        'description': 'A domain-specific ballistics calculator for archers. Configure your arrow components — shaft, point, fletching — and get real-world kinetic energy, momentum, and ethical harvest thresholds by game animal. Users save and compare custom builds.',
        'tech': ['Django', 'PostgreSQL', 'Python', 'Railway'],
        'live_url': 'https://archeryanswers-production.up.railway.app',
        'github_url': 'https://github.com/jemrich18/archery-answers',
        'category': 'Full Stack',
        'image': 'portfolio_app/images/archery.jpg',
    },
    {
        'title': 'Personal Finance Dashboard',
        'description': 'End-to-end personal finance analysis covering 1,500 transactions across 5 years. Full data pipeline from raw CSV through SQL analysis to interactive deployment, including a 6-month linear regression forecast. Shows the data engineering foundation behind the more complex production apps.',
        'tech': ['Python', 'Pandas', 'Plotly', 'Streamlit', 'Scikit-learn'],
        'live_url': 'https://end-to-end-finance-data-analysis-4qjvmptdvwcv5mcrfkydze.streamlit.app/',
        'github_url': 'https://github.com/jemrich18/end-to-end-finance-data-analysis',
        'category': 'Data Analysis',
        'image': 'portfolio_app/images/endtoend.jpg',
    },
]

SKILLS = {
    'AI / LLM': ['LangChain', 'LangGraph', 'OpenAI API', 'ChromaDB', 'RAG Pipelines', 'Prompt Engineering'],
    'Backend': ['Django', 'Django REST Framework', 'Python', 'Flask', 'REST API Design'],
    'Frontend': ['React', 'JavaScript', 'HTML', 'CSS'],
    'Database': ['PostgreSQL', 'SQLite', 'SQL'],
    'Tools & DevOps': ['Railway', 'Docker', 'Git', 'GitHub', 'GitHub Actions', 'CI/CD', 'pytest'],
    'Data Analysis': ['Pandas', 'NumPy', 'Plotly', 'Streamlit', 'Scikit-learn'],
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
    return render(request, 'portfolio_app/home.html', {
        'projects': PROJECTS,
        'skills': SKILLS,
    })


def projects(request):
    return render(request, 'portfolio_app/projects.html', {
        'projects': PROJECTS,
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
