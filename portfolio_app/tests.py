from django.test import TestCase, Client


class HomeViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_page_loads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_uses_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'portfolio_app/home.html')

    def test_home_contains_projects(self):
        response = self.client.get('/')
        self.assertIn('projects', response.context)

    def test_home_contains_skills(self):
        response = self.client.get('/')
        self.assertIn('skills', response.context)


class ProjectsViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_projects_page_loads(self):
        response = self.client.get('/projects/')
        self.assertEqual(response.status_code, 200)

    def test_projects_uses_correct_template(self):
        response = self.client.get('/projects/')
        self.assertTemplateUsed(response, 'portfolio_app/projects.html')

    def test_projects_context_contains_projects(self):
        response = self.client.get('/projects/')
        self.assertIn('projects', response.context)
        self.assertGreater(len(response.context['projects']), 0)


class AboutViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_about_page_loads(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_about_uses_correct_template(self):
        response = self.client.get('/about/')
        self.assertTemplateUsed(response, 'portfolio_app/about.html')

    def test_about_contains_skills(self):
        response = self.client.get('/about/')
        self.assertIn('skills', response.context)


class ContactViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_contact_page_loads(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

    def test_contact_uses_correct_template(self):
        response = self.client.get('/contact/')
        self.assertTemplateUsed(response, 'portfolio_app/contact.html')

    def test_contact_post_missing_fields(self):
        response = self.client.post('/contact/', {
            'name': 'Test User',
            'email': 'test@example.com'
        })
        self.assertEqual(response.status_code, 200)


class ProjectDataTest(TestCase):
    def test_projects_have_required_fields(self):
        from portfolio_app.views import PROJECTS
        for project in PROJECTS:
            self.assertIn('title', project)
            self.assertIn('description', project)
            self.assertIn('tech', project)
            self.assertIn('live_url', project)
            self.assertIn('category', project)

    def test_skills_have_categories(self):
        from portfolio_app.views import SKILLS
        self.assertGreater(len(SKILLS), 0)
        for category, skills in SKILLS.items():
            self.assertIsInstance(skills, list)
            self.assertGreater(len(skills), 0)