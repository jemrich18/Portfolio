from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings 

# Create your views here.
PROJECTS = [
    {
        'title': 'WeatherRack',
        'description': 'A Django web app that scores 10-day weather forecasts against the variables that actually drive deer movement — wind, pressure, temperature swing, and moon phase. Returns a ranked list of your best hunting days so you stop guessing. Features location management and a responsive dark UI.',
        'tech': ['Django', 'Python', 'Railway'],
        'live_url': 'https://www.theweatherrack.com',
        'github_url': 'https://github.com/jemrich18',
        'category': 'Full Stack',
        'image': 'portfolio_app/images/weatherrack.jpg',
    },
    {
        'title': 'Archery Answers',
        'description': 'A domain-specific ballistics calculator for archers. Configure your arrow components — shaft, point, fletching — and get real-world speed, kinetic energy, and momentum results. Users save and compare custom builds. Built for a real community that cares about precision.',
        'tech': ['Django', 'PostgreSQL', 'Python', 'Railway'],
        'live_url': 'https://archeryanswers-production.up.railway.app',
        'github_url': 'https://github.com/jemrich18',
        'category': 'Full Stack',
        'image': 'portfolio_app/images/archery.jpg',
    },
    {
        'title': 'GolfBros',
        'description': 'A full-stack golf community platform where players log rounds, share course reviews, and track performance over time. Built with Django REST Framework, React, and PostgreSQL. Features user authentication, full CRUD, and a clean responsive UI.',
        'tech': ['Django REST Framework', 'React', 'PostgreSQL', 'Railway'],
        'live_url': 'https://www.golfbros.org',
        'github_url': 'https://github.com/jemrich18',
        'category': 'Full Stack',
        'image': 'portfolio_app/images/golfbros.jpg',
    },
    {
        'title': 'Budget App',
        'description': 'A full-stack personal finance tracker with a Django REST Framework backend and React frontend. Features token authentication, category management, full CRUD, and expense visualization with chart breakdowns. Deployed on Railway.',
        'tech': ['Django REST Framework', 'React', 'PostgreSQL', 'Railway'],
        'live_url': 'https://budgetappreactdrf-production.up.railway.app',
        'github_url': 'https://github.com/jemrich18/budget_app_react_drf',
        'category': 'Full Stack',
        'image': 'portfolio_app/images/budget.jpg',
    },
    {
        'title': 'Hunting AI Assistant',
        'description': 'A domain-specific AI agent for hunters built with LangGraph and Django. Routes complex queries through a structured knowledge base using a multi-node state graph — covering OTC tags by state, rut timing, bow tuning, kinetic energy, and wildlife regulations. Engineered specifically to prevent hallucination on regulation-sensitive topics.',
        'tech': ['Django', 'LangGraph', 'LangChain', 'OpenAI', 'DRF', 'Railway'],
        'live_url': 'https://www.aihuntingchat.com',
        'github_url': 'https://github.com/jemrich18/Ai_agent',
        'category': 'AI / Full Stack',
        'image': 'portfolio_app/images/ai.jpg',
    },
    {
    'title': 'Job Application Assistant',
    'description': 'Built for developers in job search mode. Upload your resume and a job posting — the app scores your match percentage, surfaces your exact skill gaps, and generates a tailored cover letter. Built on a full RAG pipeline: PDF parsing, vector embedding, retrieval, and GPT-4o-mini completion with structured output.',
    'tech': ['Django', 'OpenAI', 'RAG', 'pdfplumber', 'Python', 'Railway'],
    'live_url': 'https://www.fitformyrole.com',
    'github_url': 'https://github.com/jemrich18/rag_application_assistant',
    'category': 'AI / Full Stack',
    'image': 'portfolio_app/images/rag.jpg',
    },
]

SKILLS = {
    'Backend': ['Django', 'Django REST Framework', 'Python', 'Flask'],
    'Frontend': ['React', 'HTML', 'CSS', 'JavaScript'],
    'Database': ['PostgreSQL', 'SQLite', 'SQL'],
    'Tools & DevOps': ['Railway', 'Git', 'GitHub', 'VS Code', 'Docker'],
    'AI / ML': ['LangChain', 'LangGraph', 'OpenAI API', 'Streamlit'],
    'Languages': ['Python', 'JavaScript', 'Java', 'SQL'],
}

EDUCATION = [
    {
        'degree': 'B.S. Computer Science — In Progress',
        'school': 'University of Maryland Global Campus',
        'details': 'Algorithms, Problem Solving, Intro to Java',
    },
    {
        'degree': 'Full Stack Development',
        'school': 'Codecademy',
        'details': 'Python, Django, JavaScript, SQL, HTML, Flask — all completed at 100%',
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
