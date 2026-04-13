from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings 

# Create your views here.
PROJECTS = [
    {
        'title': 'WeatherRack',
        'description': 'A Django web app that analyzes 10-day weather forecasts to score and rank the best days to hunt based on conditions that drive deer movement. Features location management, moon data, and a responsive dark UI.',
        'tech': ['Django', 'Python', 'Railway'],
        'live_url': 'https://www.weatherrack.com',
        'github_url': 'https://github.com/jemrich18',
        'category': 'Full Stack',
        'image': 'portfolio_app/images/weatherrack.jpg',
    },
    {
        'title': 'Archery Answers',
        'description': 'A bowhunting ballistics platform that calculates real-world arrow speed, kinetic energy, and momentum to help archers build the perfect hunting setup.',
        'tech': ['Django', 'PostgreSQL', 'Python', 'Railway'],
        'live_url': 'https://archeryanswers-production.up.railway.app',
        'github_url': 'https://github.com/jemrich18',
        'category': 'Full Stack',
        'image': 'portfolio_app/images/archery.jpg',
    },
    {
        'title': 'GolfBros',
        'description': 'A full-stack blog platform for golfers to share round reviews and course conditions, built with Django REST Framework and React.',
        'tech': ['Django REST Framework', 'React', 'PostgreSQL', 'Railway'],
        'live_url': 'https://www.golfbros.org',
        'github_url': 'https://github.com/jemrich18',
        'category': 'Full Stack',
        'image': 'portfolio_app/images/golfbros.jpg',
    },
    {
        'title': 'Budget App',
        'description': 'A full-stack budget tracking platform that allows users to categorize and track expenses and incomes.',
        'tech': ['Django REST Framework', 'React', 'PostgreSQL', 'Railway'],
        'live_url': 'https://budgetappreactdrf-production.up.railway.app',
        'github_url': 'https://github.com/jemrich18/budget_app_react_drf',
        'category': 'Full Stack',
        'image': 'portfolio_app/images/budget.jpg',
    },
    {
        'title': 'Hunting AI Assistant',
        'description': 'An AI-powered hunting assistant built with Django, LangGraph, and OpenAI GPT-4o-mini. Uses a structured knowledge base to answer questions about OTC tag availability by state, bow tuning fixes, rut phases, kinetic energy requirements, and preference point systems.',
        'tech': ['Django', 'LangGraph', 'LangChain', 'OpenAI', 'DRF', 'Railway'],
        'live_url': 'https://www.aihuntingchat.com',
        'github_url': 'https://github.com/jemrich18/Ai_agent',
        'category': 'AI / Full Stack',
        'image': 'portfolio_app/images/ai.jpg',
    },
    {
    'title': 'Job Application Assistant',
    'description': 'An AI-powered RAG application that analyzes your resume against job descriptions, scores your match, identifies skill gaps, generates tailored cover letters, and recommends the best developer roles for your current skillset.',
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
