from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
PROJECTS = [
    {
        'title': 'Erin the Estie',
        'description': 'A full-stack booking platform built for a real paying client — an esthetician who needed scheduling without a subscription fee. Custom appointment system with an approval workflow, service menu management, and a mobile-optimized admin dashboard. Requirements through deployment, owned end to end.',
        'tech': ['Django', 'PostgreSQL', 'Gmail SMTP', 'Railway'],
        'highlight': 'STATUS: LIVE — PAYING CLIENT · ROLE: Solo build, full SDLC',
        'live_url': 'https://www.erintheestie.com',
        'github_url': '',  # private client repo — leave blank, template hides the button
        'image': 'portfolio_app/images/estie.jpg',
    },
    {
        'title': 'Fit For My Role',
        'description': 'A retrieval-augmented generation pipeline: resumes are parsed with pdfplumber, chunked, and embedded into a ChromaDB vector store. The most relevant chunks are retrieved by similarity search against a job description to ground GPT-4o-mini\u2019s skill-match scoring and generated cover letter in the candidate\u2019s real experience — not general knowledge.',
        'tech': ['Django', 'OpenAI API', 'ChromaDB', 'pdfplumber'],
        'highlight': 'STATUS: LIVE · PIPELINE: pdfplumber \u2192 embeddings \u2192 ChromaDB \u2192 retrieval \u2192 GPT-4o-mini',
        'live_url': 'https://www.fitformyrole.com',
        'github_url': 'https://github.com/jemrich18/rag_application_assistant',
        'image': 'portfolio_app/images/rag.jpg',
    },
    {
        'title': 'TrackMyHandicap',
        'description': 'A Django REST Framework API implementing the full WHS golf handicap formula from user-submitted rounds — a free alternative to a $60/year official subscription. JWT-authenticated, with a separate React/TypeScript frontend and Stripe integrated for a planned premium tier with extended trend analysis by course and weather condition.',
        'tech': ['Django REST Framework', 'React', 'TypeScript', 'Stripe'],
        'highlight': 'STATUS: LIVE · AUTH: JWT · BILLING: Stripe integrated, premium tier planned',
        'live_url': 'https://trackmyhandi.com',
        'github_url': 'https://github.com/jemrich18/trackmyhandi',
        'image': 'portfolio_app/images/trackmyhandi.jpg',
    },
    {
        'title': 'OurCushion',
        'description': 'A real-time shared household finance tracker built around instant accountability — no bank linking, just an honest running balance based on what\u2019s actually logged. Self-service registration lets any household sign up and get started. Expense and balance updates push instantly to both partners via Django Channels and Redis, with graceful degradation built in: if a WebSocket connection can\u2019t reach Redis, the app still works fully on standard page loads.',
        'tech': ['Django', 'Django Channels', 'WebSockets', 'Redis', 'PostgreSQL'],
        'highlight': 'STATUS: LIVE · REAL-TIME: Channels + Redis, graceful degradation on connection drop · AUTH: Self-service registration',
        'live_url': 'https://ourcushion.com',
        'github_url': 'https://github.com/jemrich18/household_budget',
        'image': 'portfolio_app/images/ourcushion.jpg',
    },
]

SKILLS = {
    'Backend': ['Django', 'Django REST Framework', 'Python', 'Django Channels', 'WebSockets', 'Redis', 'REST API Design'],
    'Frontend': ['React', 'JavaScript', 'TypeScript', 'HTML', 'CSS'],
    'Database': ['PostgreSQL', 'SQLite', 'SQL'],
    'Tools & DevOps': ['Railway', 'Docker', 'Git', 'GitHub Actions', 'CI/CD', 'pytest'],
    'AI / LLM': ['OpenAI API', 'ChromaDB', 'RAG Pipelines', 'Vector Embeddings', 'Prompt Engineering'],
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