# Week-by-Week Detailed Breakdown


---

# WEEK 1: Foundation & Core Pages

## 🎯 Week 1 Goals
- Setup complete development environment
- Understand Flask basics and project structure
- Create database schema and models
- Build all core pages (Home, About, Projects, Blog, Contact)
- Get comfortable with Jinja2 templating

---

## **DAY 1: Project Setup & Environment** (April 25)

### Morning Tasks
```
⏱️ Expected Time: 3-4 hours
```

#### 1.1 Create Project Structure
```bash
cd c:\Users\dibya\Python\Personal\PersonalWebsite

# Create folders
mkdir templates
mkdir static
mkdir static/css
mkdir static/js
mkdir static/images
mkdir database

# Create main files
touch app.py
touch config.py
touch requirements.txt
touch .gitignore
touch README.md
```

#### 1.2 Setup Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# You should see (venv) in terminal
```

#### 1.3 Create requirements.txt

```txt
Flask==3.0.0
Flask-SQLAlchemy==3.1.1
python-dotenv==1.0.0
gunicorn==21.2.0
Werkzeug==3.0.0
email-validator==2.0.0
```

#### 1.4 Install Dependencies
```bash
pip install -r requirements.txt
```

#### 1.5 Initialize Git Repository
```bash
git init
git config user.name "Your Name"
git config user.email "your.email@example.com"

# Create .gitignore
type nul > .gitignore
```

Add to `.gitignore`:
```
venv/
__pycache__/
*.pyc
.env
*.db
.DS_Store
.vscode/
```

#### 1.6 Create Basic app.py

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///personal_website.db'
app.config['SECRET_KEY'] = 'dev-key-change-later'

db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

#### 1.7 Test It Works
```bash
# Start Flask development server
python app.py

# Visit: http://localhost:5000
# You should see: "Hello World!"
```

### Afternoon Tasks

#### 1.8 Learning: Flask Basics
**Read & Understand:**
- What is a route? (URL to function mapping)
- What is a view function? (handles requests)
- What is debug mode? (auto-reload, detailed errors)

#### 1.9 Create .env File
```env
FLASK_ENV=development
SECRET_KEY=temporary-dev-key-only
DEBUG=True
```

#### 1.10 Initial Git Commit
```bash
git add .
git commit -m "Initial project setup with Flask and virtual environment"
```

### 📚 Day 1 Learning Focus
- **What you learned**: Python virtual environments, Flask app structure, pip packages
- **Key concepts**: VENV isolation, requirements.txt, Flask routing
- **Questions to answer**: Why use virtual environment? What does requirements.txt do?

### ⏸️ Day 1 Checkpoint
```
✅ Virtual environment working
✅ Flask app runs without errors
✅ Git initialized with initial commit
✅ Project structure created
```

---

## **DAY 2: Database Setup & Models** (April 26)

### Morning Tasks
```
⏱️ Expected Time: 3-4 hours
```

#### 2.1 Create Database Models

Create `database/models.py`:

```python
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

db = SQLAlchemy()

# User Model (for admin login - optional for Week 1)
class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<User {self.email}>'

# Project Model
class Project(db.Model):
    __tablename__ = 'projects'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    technologies = db.Column(db.String(500))  # comma-separated
    github_url = db.Column(db.String(500))
    demo_url = db.Column(db.String(500))
    image_url = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Project {self.title}>'

# Blog Post Model
class BlogPost(db.Model):
    __tablename__ = 'blog_posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    slug = db.Column(db.String(300), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    excerpt = db.Column(db.String(500))
    image_url = db.Column(db.String(500))
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<BlogPost {self.title}>'

# Contact Message Model
class ContactMessage(db.Model):
    __tablename__ = 'contact_messages'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(300), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<ContactMessage from {self.name}>'
```

#### 2.2 Update app.py

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from database.models import db  # Import db

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///personal_website.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-key-change-later')

db.init_app(app)

@app.route('/')
def index():
    return 'Flask + Database ready!'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Creates all tables
        print("Database initialized!")
    app.run(debug=True)
```

#### 2.3 Test Database Creation

```bash
python app.py

# You should see:
# "Database initialized!"
# And a personal_website.db file appears
```

### Afternoon Tasks

#### 2.4 Create Database Initialization Script

Create `database/init_db.py`:

```python
from app import app, db
from database.models import Project, BlogPost, User
from datetime import datetime

def init_sample_data():
    """Add sample data for development"""
    
    with app.app_context():
        # Clear existing data
        Project.query.delete()
        BlogPost.query.delete()
        db.session.commit()
        
        # Add sample projects
        project1 = Project(
            title="Personal Website",
            description="A portfolio website built with Flask and SQLite. Features responsive design, blog functionality, and project showcase.",
            technologies="Python, Flask, SQLAlchemy, Bootstrap, SQLite",
            github_url="https://github.com/yourusername/personal-website",
            demo_url="https://yourwebsite.onrender.com",
            image_url="/static/images/website-preview.jpg"
        )
        
        project2 = Project(
            title="Python Automation Tool",
            description="An automation script that processes data from CSV files and generates reports.",
            technologies="Python, Pandas, Openpyxl",
            github_url="https://github.com/yourusername/automation-tool",
            image_url="/static/images/automation-preview.jpg"
        )
        
        db.session.add(project1)
        db.session.add(project2)
        
        # Add sample blog post
        post1 = BlogPost(
            title="Getting Started with Flask",
            slug="getting-started-with-flask",
            content="Flask is a lightweight web framework...",
            excerpt="Learn the basics of Flask web framework.",
            image_url="/static/images/blog1.jpg"
        )
        
        db.session.add(post1)
        db.session.commit()
        
        print("✅ Sample data added successfully!")

if __name__ == '__main__':
    init_sample_data()
```

#### 2.5 Run Sample Data Script

```bash
python database/init_db.py

# You should see:
# "✅ Sample data added successfully!"
```

### 📚 Day 2 Learning Focus
- **What you learned**: SQLAlchemy ORM, Database models, Relationships, Primary keys
- **Key concepts**: 
  - Model definition with columns and data types
  - DateTime fields
  - Unique constraints
  - __repr__ methods for debugging

### ⏸️ Day 2 Checkpoint
```
✅ Database models created
✅ Database file generated
✅ Sample data inserted
✅ Models verified in code
```

---

## **DAY 3-4: Templates & Static Files** (April 27-28)

### Goals
- Create base template with Bootstrap
- Setup CSS styling
- Create static folder structure
- Test template inheritance

### 3.1 Download Bootstrap

Create `templates/base.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}My Personal Website{% endblock %}</title>
    
    <!-- Bootstrap CSS from CDN -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    
    {% block extra_css %}{% endblock %}
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark sticky-top">
        <div class="container">
            <a class="navbar-brand" href="/">YourName</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item"><a class="nav-link" href="/">Home</a></li>
                    <li class="nav-item"><a class="nav-link" href="/about">About</a></li>
                    <li class="nav-item"><a class="nav-link" href="/projects">Projects</a></li>
                    <li class="nav-item"><a class="nav-link" href="/blog">Blog</a></li>
                    <li class="nav-item"><a class="nav-link" href="/contact">Contact</a></li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Main Content -->
    <main>
        {% block content %}{% endblock %}
    </main>

    <!-- Footer -->
    <footer class="bg-dark text-white text-center py-4 mt-5">
        <div class="container">
            <p>&copy; 2026 Your Name. All rights reserved.</p>
            <p>
                <a href="#" class="text-white-50">Twitter</a> |
                <a href="#" class="text-white-50">LinkedIn</a> |
                <a href="#" class="text-white-50">GitHub</a>
            </p>
        </div>
    </footer>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="{{ url_for('static', filename='js/script.js') }}"></script>
    
    {% block extra_js %}{% endblock %}
</body>
</html>
```

### 3.2 Create CSS File

Create `static/css/style.css`:

```css
:root {
    --primary-color: #007bff;
    --secondary-color: #6c757d;
    --success-color: #28a745;
    --danger-color: #dc3545;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: #f8f9fa;
    color: #333;
}

/* Header Styling */
.navbar-brand {
    font-weight: bold;
    font-size: 1.5rem;
}

/* Main Content */
main {
    min-height: calc(100vh - 200px);
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Hero Section */
.hero {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 4rem 0;
    text-align: center;
    margin-bottom: 3rem;
}

.hero h1 {
    font-size: 3rem;
    margin-bottom: 1rem;
    font-weight: bold;
}

.hero p {
    font-size: 1.25rem;
    margin-bottom: 2rem;
}

/* Cards */
.card {
    border: none;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    margin-bottom: 1.5rem;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 12px rgba(0, 0, 0, 0.15);
}

/* Buttons */
.btn-primary {
    background-color: var(--primary-color);
    border-color: var(--primary-color);
}

.btn-primary:hover {
    background-color: #0056b3;
    border-color: #0056b3;
}

/* Footer */
footer {
    margin-top: auto;
}

footer a {
    text-decoration: none;
    transition: color 0.3s ease;
}

footer a:hover {
    color: white !important;
}

/* Forms */
.form-control:focus {
    border-color: var(--primary-color);
    box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
}

/* Responsive */
@media (max-width: 768px) {
    .hero h1 {
        font-size: 2rem;
    }
    
    .hero p {
        font-size: 1rem;
    }
}
```

### 3.3 Create JavaScript File

Create `static/js/script.js`:

```javascript
// Add interactivity here

document.addEventListener('DOMContentLoaded', function() {
    console.log('Personal website loaded!');
    
    // Example: Form validation
    const forms = document.querySelectorAll('.needs-validation');
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });
});
```

### 3.4 Update Flask App to Use Templates

Update `app.py`:

```python
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from database.models import db

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///personal_website.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-key-change-later')

db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

### 📚 Day 3-4 Learning Focus
- **What you learned**: Jinja2 templating, Template inheritance, Bootstrap basics
- **Key concepts**: 
  - `{% block %}` for extensible sections
  - `{{ }}` for variables
  - `url_for()` for dynamic URLs
  - Bootstrap grid system

### ⏸️ Day 3-4 Checkpoint
```
✅ Base template created with navigation
✅ CSS styling implemented
✅ JavaScript file ready
✅ Template inheritance working
✅ Flask app serves templates
```

---

## **DAY 5-7: Build Core Pages** (April 29 - May 1)

### Goals
- Create all 5 main pages
- Implement database queries
- Add forms for contact
- Test all navigation

### 5.1 Home Page (index.html)

Create `templates/index.html`:

```html
{% extends "base.html" %}

{% block title %}Home - My Personal Website{% endblock %}

{% block content %}
<!-- Hero Section -->
<section class="hero">
    <div class="container">
        <h1>Hi, I'm Your Name</h1>
        <p>Full Stack Developer | Problem Solver | Tech Enthusiast</p>
        <a href="/projects" class="btn btn-light btn-lg">View My Work</a>
    </div>
</section>

<!-- Featured Projects -->
<section class="py-5">
    <div class="container">
        <h2 class="mb-4">Featured Projects</h2>
        <div class="row">
            <div class="col-md-6 col-lg-4">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">Project 1</h5>
                        <p class="card-text">A brief description of your project goes here.</p>
                        <a href="/projects" class="btn btn-primary btn-sm">Learn More</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Call to Action -->
<section class="bg-primary text-white py-5">
    <div class="container text-center">
        <h2>Let's Work Together</h2>
        <p>Feel free to reach out for collaborations</p>
        <a href="/contact" class="btn btn-light btn-lg">Get In Touch</a>
    </div>
</section>

{% endblock %}
```

### 5.2 About Page (about.html)

Create `templates/about.html`:

```html
{% extends "base.html" %}

{% block title %}About - My Personal Website{% endblock %}

{% block content %}
<div class="container py-5">
    <div class="row">
        <div class="col-lg-8 offset-lg-2">
            <h1 class="mb-4">About Me</h1>
            
            <p class="lead">
                Welcome! I'm a passionate developer with expertise in Python, web development, and modern technologies.
            </p>
            
            <h3 class="mt-5 mb-3">My Background</h3>
            <p>
                I started my programming journey with Python and fell in love with it. 
                Over the years, I've worked on various projects including web applications, 
                automation scripts, and data analysis tools.
            </p>
            
            <h3 class="mt-5 mb-3">Skills</h3>
            <div class="row">
                <div class="col-md-6">
                    <h5>Backend</h5>
                    <ul>
                        <li>Python</li>
                        <li>Flask</li>
                        <li>SQLite/PostgreSQL</li>
                    </ul>
                </div>
                <div class="col-md-6">
                    <h5>Frontend</h5>
                    <ul>
                        <li>HTML5</li>
                        <li>CSS3</li>
                        <li>Bootstrap</li>
                    </ul>
                </div>
            </div>
            
            <h3 class="mt-5 mb-3">What I Love</h3>
            <p>
                I love solving complex problems, learning new technologies, and building applications 
                that make a difference. When I'm not coding, you can find me exploring open-source projects 
                or contributing to the developer community.
            </p>
            
            <hr class="my-5">
            <p class="text-center text-muted">
                <a href="/contact" class="text-decoration-none">Interested in working together? Let's talk!</a>
            </p>
        </div>
    </div>
</div>
{% endblock %}
```

### 5.3 Projects Page (projects.html)

Create `templates/projects.html`:

```html
{% extends "base.html" %}

{% block title %}Projects - My Personal Website{% endblock %}

{% block content %}
<div class="container py-5">
    <h1 class="mb-5">My Projects</h1>
    
    <div class="row">
        <div class="col-md-6 col-lg-4">
            <div class="card h-100">
                <div class="card-body">
                    <h5 class="card-title">Personal Website</h5>
                    <p class="card-text">
                        A portfolio website built with Flask and SQLite. Features responsive design, blog functionality, and project showcase.
                    </p>
                    <p class="card-text">
                        <small class="text-muted">
                            <strong>Tech:</strong> Python, Flask, SQLAlchemy, Bootstrap, SQLite
                        </small>
                    </p>
                </div>
                <div class="card-footer bg-white border-top-0">
                    <a href="#" class="btn btn-sm btn-outline-primary">View Demo</a>
                    <a href="#" class="btn btn-sm btn-outline-secondary">GitHub</a>
                </div>
            </div>
        </div>
    </div>
    
    <p class="text-center mt-5 text-muted">More projects coming soon...</p>
</div>
{% endblock %}
```

### 5.4 Blog Page (blog.html)

Create `templates/blog.html`:

```html
{% extends "base.html" %}

{% block title %}Blog - My Personal Website{% endblock %}

{% block content %}
<div class="container py-5">
    <h1 class="mb-5">Blog</h1>
    
    <div class="row">
        <div class="col-lg-8 offset-lg-2">
            <article class="mb-5 pb-5 border-bottom">
                <h3><a href="#" class="text-decoration-none">Getting Started with Flask</a></h3>
                <small class="text-muted">Published on <strong>April 25, 2026</strong></small>
                <p class="mt-3">
                    Flask is a lightweight and versatile Python web framework. 
                    In this post, I'll cover the basics of setting up a Flask application...
                </p>
                <a href="#" class="btn btn-sm btn-outline-primary">Read More</a>
            </article>
        </div>
    </div>
    
    <p class="text-center mt-5 text-muted">More blog posts coming soon...</p>
</div>
{% endblock %}
```

### 5.5 Contact Page (contact.html)

Create `templates/contact.html`:

```html
{% extends "base.html" %}

{% block title %}Contact - My Personal Website{% endblock %}

{% block content %}
<div class="container py-5">
    <div class="row">
        <div class="col-lg-6 offset-lg-3">
            <h1 class="mb-5 text-center">Get In Touch</h1>
            
            <form method="POST" action="/submit_contact" class="needs-validation" novalidate>
                <div class="mb-3">
                    <label for="name" class="form-label">Your Name</label>
                    <input type="text" class="form-control" id="name" name="name" required>
                    <div class="invalid-feedback">Please provide a name.</div>
                </div>
                
                <div class="mb-3">
                    <label for="email" class="form-label">Email Address</label>
                    <input type="email" class="form-control" id="email" name="email" required>
                    <div class="invalid-feedback">Please provide a valid email.</div>
                </div>
                
                <div class="mb-3">
                    <label for="subject" class="form-label">Subject</label>
                    <input type="text" class="form-control" id="subject" name="subject" required>
                    <div class="invalid-feedback">Please provide a subject.</div>
                </div>
                
                <div class="mb-3">
                    <label for="message" class="form-label">Message</label>
                    <textarea class="form-control" id="message" name="message" rows="5" required></textarea>
                    <div class="invalid-feedback">Please provide a message.</div>
                </div>
                
                <button type="submit" class="btn btn-primary w-100">Send Message</button>
            </form>
            
            <hr class="my-5">
            
            <h4 class="text-center">Or Connect With Me</h4>
            <div class="text-center">
                <a href="#" class="btn btn-outline-primary me-2">Twitter</a>
                <a href="#" class="btn btn-outline-primary me-2">LinkedIn</a>
                <a href="#" class="btn btn-outline-primary">GitHub</a>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

### 5.6 Add Contact Form Handler

Update `app.py` to handle contact form:

```python
from flask import request, redirect, url_for, flash
from database.models import ContactMessage

# ... existing code ...

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject')
    message = request.form.get('message')
    
    if not all([name, email, subject, message]):
        flash('Please fill in all fields', 'error')
        return redirect(url_for('contact'))
    
    contact = ContactMessage(
        name=name,
        email=email,
        subject=subject,
        message=message
    )
    
    db.session.add(contact)
    db.session.commit()
    
    flash('Message sent successfully! I\'ll get back to you soon.', 'success')
    return redirect(url_for('contact'))
```

### 5.7 Test Everything

```bash
# Activate venv if not already
venv\Scripts\activate

# Run the app
python app.py

# Visit in browser:
# http://localhost:5000/
# http://localhost:5000/about
# http://localhost:5000/projects
# http://localhost:5000/blog
# http://localhost:5000/contact
```

### 📚 Day 5-7 Learning Focus
- **What you learned**: Forms in Flask, Request handling, Database operations
- **Key concepts**:
  - GET vs POST requests
  - Form validation
  - Template variables
  - Redirects and flashes

### ⏸️ Week 1 Final Checkpoint
```
✅ All 5 main pages created
✅ Database working with SQLite
✅ Forms handling contact submissions
✅ Navigation working across all pages
✅ Styling responsive on mobile
✅ Code committed to Git with meaningful commits
```

### 🎯 End of Week 1 Summary

**What You've Built:**
- Complete Flask application with 5 pages
- SQLite database with proper schema
- Form handling and validation
- Responsive Bootstrap styling
- Professional navigation

**What You've Learned:**
- Flask routing and views
- Jinja2 templating
- SQLAlchemy ORM
- HTML/CSS with Bootstrap
- Database design basics
- Git version control

**Time to Review:**
- All pages working?
- Navigation smooth?
- Database queries functional?
- Forms submitting correctly?

---

# WEEK 2: Features & Deployment

## 🎯 Week 2 Goals
- Add dynamic content from database
- Implement admin features
- Production-ready security
- Deploy to Render.com
- Test in production

---

## **DAY 8-9: Dynamic Content & Features** (May 2-3)

### 8.1 Update Projects Page with Database

Update `app.py`:

```python
from database.models import Project, BlogPost

@app.route('/projects')
def projects():
    projects = Project.query.all()
    return render_template('projects.html', projects=projects)
```

Update `templates/projects.html`:

```html
{% extends "base.html" %}

{% block title %}Projects - My Personal Website{% endblock %}

{% block content %}
<div class="container py-5">
    <h1 class="mb-5">My Projects</h1>
    
    {% if projects %}
    <div class="row">
        {% for project in projects %}
        <div class="col-md-6 col-lg-4">
            <div class="card h-100">
                <div class="card-body">
                    <h5 class="card-title">{{ project.title }}</h5>
                    <p class="card-text">{{ project.description[:150] }}...</p>
                    <p class="card-text">
                        <small class="text-muted">
                            <strong>Tech:</strong> {{ project.technologies }}
                        </small>
                    </p>
                </div>
                <div class="card-footer bg-white border-top-0">
                    {% if project.demo_url %}
                    <a href="{{ project.demo_url }}" class="btn btn-sm btn-outline-primary" target="_blank">View Demo</a>
                    {% endif %}
                    {% if project.github_url %}
                    <a href="{{ project.github_url }}" class="btn btn-sm btn-outline-secondary" target="_blank">GitHub</a>
                    {% endif %}
                </div>
            </div>
        </div>
        {% endfor %}
    </div>
    {% else %}
    <p class="text-center text-muted">No projects yet. Check back soon!</p>
    {% endif %}
</div>
{% endblock %}
```

### 8.2 Update Blog Page with Database

Update `app.py`:

```python
@app.route('/blog')
def blog():
    posts = BlogPost.query.order_by(BlogPost.published_at.desc()).all()
    return render_template('blog.html', posts=posts)

@app.route('/blog/<slug>')
def blog_post(slug):
    post = BlogPost.query.filter_by(slug=slug).first_or_404()
    return render_template('blog_post.html', post=post)
```

Update `templates/blog.html`:

```html
{% extends "base.html" %}

{% block title %}Blog - My Personal Website{% endblock %}

{% block content %}
<div class="container py-5">
    <h1 class="mb-5">Blog</h1>
    
    {% if posts %}
    <div class="row">
        <div class="col-lg-8 offset-lg-2">
            {% for post in posts %}
            <article class="mb-5 pb-5 border-bottom">
                <h3><a href="/blog/{{ post.slug }}" class="text-decoration-none">{{ post.title }}</a></h3>
                <small class="text-muted">Published on <strong>{{ post.published_at.strftime('%B %d, %Y') }}</strong></small>
                <p class="mt-3">{{ post.excerpt or post.content[:200] }}...</p>
                <a href="/blog/{{ post.slug }}" class="btn btn-sm btn-outline-primary">Read More</a>
            </article>
            {% endfor %}
        </div>
    </div>
    {% else %}
    <p class="text-center text-muted">No blog posts yet. Check back soon!</p>
    {% endif %}
</div>
{% endblock %}
```

Create `templates/blog_post.html`:

```html
{% extends "base.html" %}

{% block title %}{{ post.title }} - My Blog{% endblock %}

{% block content %}
<div class="container py-5">
    <div class="row">
        <div class="col-lg-8 offset-lg-2">
            <a href="/blog" class="text-decoration-none mb-3">← Back to Blog</a>
            
            <article>
                <h1 class="mb-2">{{ post.title }}</h1>
                <small class="text-muted">Published on {{ post.published_at.strftime('%B %d, %Y') }}</small>
                
                <hr class="my-4">
                
                <div class="post-content">
                    {{ post.content }}
                </div>
                
                <hr class="my-4">
                
                <p><a href="/contact" class="btn btn-primary">Leave a Comment</a></p>
            </article>
        </div>
    </div>
</div>
{% endblock %}
```

### 8.3 Add Admin Features (Optional)

Create `templates/admin/login.html`:

```html
{% extends "base.html" %}

{% block title %}Admin Login{% endblock %}

{% block content %}
<div class="container py-5">
    <div class="row">
        <div class="col-md-4 offset-md-4">
            <h2 class="text-center mb-4">Admin Login</h2>
            
            <form method="POST" action="/admin/login" class="needs-validation" novalidate>
                <div class="mb-3">
                    <label for="email" class="form-label">Email</label>
                    <input type="email" class="form-control" id="email" name="email" required>
                </div>
                
                <div class="mb-3">
                    <label for="password" class="form-label">Password</label>
                    <input type="password" class="form-control" id="password" name="password" required>
                </div>
                
                <button type="submit" class="btn btn-primary w-100">Login</button>
            </form>
        </div>
    </div>
</div>
{% endblock %}
```

### 📚 Day 8-9 Learning Focus
- **What you learned**: Database queries in routes, Template loops, Dynamic URLs
- **Key concepts**: 
  - `query.all()` vs `query.first()`
  - Filtering queries
  - URL parameters
  - Conditional rendering

### ⏸️ Day 8-9 Checkpoint
```
✅ Database content showing on pages
✅ Blog post individual pages working
✅ Projects displaying dynamically
✅ Admin login page created
```

---

## **DAY 10-11: Production Preparation** (May 4-5)

### 10.1 Environment Configuration

Create `.env`:

```env
FLASK_ENV=production
SECRET_KEY=your-random-32-char-key-here
DEBUG=False
```

### 10.2 Security Improvements

Update `app.py`:

```python
from flask import session

@app.after_request
def set_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500
```

### 10.3 Error Pages

Create `templates/404.html`:

```html
{% extends "base.html" %}

{% block content %}
<div class="container py-5 text-center">
    <h1>404 - Page Not Found</h1>
    <p>Sorry, the page you're looking for doesn't exist.</p>
    <a href="/" class="btn btn-primary">Go Home</a>
</div>
{% endblock %}
```

### 10.4 Create Procfile and runtime.txt

Create `Procfile`:
```
web: gunicorn app:app
```

Create `runtime.txt`:
```
python-3.11.0
```

### 📚 Day 10-11 Learning Focus
- **What you learned**: Security headers, Error handling, Production configuration
- **Key concepts**: 
  - Environment variables
  - Security best practices
  - Error handling
  - Deployment readiness

### ⏸️ Day 10-11 Checkpoint
```
✅ Environment variables configured
✅ Security headers added
✅ Error pages created
✅ Production config ready
```

---

## **DAY 12-14: Deployment** (May 6-8)

### 12.1 Final Git Commits

```bash
git add .
git commit -m "Add dynamic content from database"
git commit -m "Add security headers and error handling"
git commit -m "Prepare for production deployment"
git push origin main
```

### 12.2 Deploy to Render.com

**Follow DEPLOYMENT_GUIDE.md** (already created)

1. Create Render account
2. Connect GitHub repository
3. Configure web service
4. Set environment variables
5. Deploy!

### 12.3 Testing in Production

```
✅ Visit your deployed URL
✅ Test all pages load
✅ Test contact form
✅ Check responsive design on mobile
✅ Verify database working
✅ Check browser console for errors
✅ Test social links
```

### 12.4 Final Polish

- Update social media links
- Add your actual profile picture
- Update "About" section with your bio
- Add your real projects
- Customize colors/styling
- Test performance

### 📚 Day 12-14 Learning Focus
- **What you learned**: Deployment process, Cloud hosting, Production debugging
- **Key concepts**: 
  - Git workflow
  - Environment configuration
  - Hosting platforms
  - Monitoring and logs

### ✨ Week 2 Final Checkpoint
```
✅ Application deployed to Render.com
✅ Custom domain (optional)
✅ All features working in production
✅ Database functional
✅ Contact form receiving messages
✅ Responsive on all devices
✅ Performance acceptable
✅ No console errors
```

---

## 🎉 Project Complete!

### 📊 What You've Accomplished

#### Architecture:
- ✅ Clean, modular Flask application
- ✅ SQLite database with proper schema
- ✅ Responsive Bootstrap frontend
- ✅ Professional navigation and layout

#### Features:
- ✅ 5+ pages (Home, About, Projects, Blog, Contact)
- ✅ Working contact form
- ✅ Project portfolio from database
- ✅ Blog posts from database
- ✅ Mobile responsive design

#### Production:
- ✅ Deployed on Render.com
- ✅ Custom domain setup (optional)
- ✅ Security implemented
- ✅ Error handling in place
- ✅ Environment configuration

#### Learning:
- ✅ Flask fundamentals
- ✅ Database design with SQLAlchemy
- ✅ Jinja2 templating
- ✅ HTML/CSS/Bootstrap
- ✅ Form handling
- ✅ Git version control
- ✅ Cloud deployment basics

### 🚀 Next Steps (After 2 Weeks)

1. **Add Comments**: Let users comment on blog posts
2. **Email Notifications**: Send yourself email when contact form submitted
3. **Admin Panel**: Manage projects and blog posts from web interface
4. **Search**: Add search functionality
5. **Analytics**: Track visitors with Google Analytics
6. **SEO**: Optimize for search engines
7. **Dark Mode**: Add theme toggle
8. **API**: Create API endpoints for future integrations

### 📚 Resources for Continuing

- **Flask**: https://flask.palletsprojects.com/
- **SQLAlchemy**: https://docs.sqlalchemy.org/
- **Bootstrap**: https://getbootstrap.com/
- **Render Docs**: https://render.com/docs
- **Web Dev Roadmap**: https://roadmap.sh/frontend
- **Python Best Practices**: https://pep8.org/

### 💪 Skills You Can Now Use

- Build Python web applications
- Design databases
- Create responsive websites
- Deploy applications to cloud
- Work with version control
- Understand web architecture

---

**Congratulations! You've built a professional personal website from scratch! 🎓**

---

## 📝 Notes for Learners

### Key Takeaways

1. **Start Small, Think Big**: Begin with basics, scale gradually
2. **Understand Each Part**: Don't just copy code, understand why it works
3. **Test Frequently**: Run your code after each change
4. **Commit Often**: Good git history helps debugging
5. **Read Error Messages**: They usually tell you exactly what's wrong
6. **Use Documentation**: Official docs are your best friend
7. **Ask for Help**: Stack Overflow, Reddit, Dev communities

### Common Mistakes to Avoid

❌ **Don't:** Commit `.env` or `venv/` to GitHub
✅ **Do:** Add them to `.gitignore`

❌ **Don't:** Use `DEBUG=True` in production
✅ **Do:** Use `DEBUG=False` and proper error handling

❌ **Don't:** Store secrets in code
✅ **Do:** Use environment variables

❌ **Don't:** Skip testing
✅ **Do:** Test each feature as you build it

❌ **Don't:** Give up when you hit errors
✅ **Do:** Read error messages carefully, they help!

---

**Ready to start? Let's build! 🚀**
