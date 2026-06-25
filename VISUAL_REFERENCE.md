# Visual Architecture & Quick Reference

## 🎯 High-Level Flow

```
User Request
    ↓
Flask Route (@app.route('/'))
    ↓
Route Handler Function
    ├─→ Query Database (if needed)
    │   ↓
    │   SQLite DB
    │   ↓
    │   Return Data
    │
    └─→ Render Template (Jinja2)
        ├─→ Load HTML file
        ├─→ Insert Python variables {{ }}
        ├─→ Loop through data {% for %}
        ├─→ Include CSS/JS links
        ↓
    HTML Response
        ↓
    Browser Renders
        ↓
    User Sees Website
```

---

## 📊 File Relationship Diagram

```
app.py (Main Application)
├── config.py (Settings)
├── database/models.py (Database Models)
│   ├── User
│   ├── Project
│   ├── BlogPost
│   └── ContactMessage
│
├── static/ (Static Files - Served As-Is)
│   ├── css/style.css
│   ├── js/script.js
│   └── images/
│
└── templates/ (HTML Files - Processed by Flask)
    ├── base.html (Parent template)
    ├── index.html
    ├── about.html
    ├── projects.html
    ├── blog.html
    ├── contact.html
    ├── blog_post.html
    ├── 404.html
    ├── 500.html
    └── admin/login.html
```

---

## 🔄 Route Flow

```
/ ────────→ index() ────→ render_template('index.html') ──→ Home Page
/about ────→ about() ────→ render_template('about.html') ──→ About Page
/projects ─→ projects() ─→ render_template('projects.html') + DB Query
/blog ─────→ blog() ────→ render_template('blog.html') + DB Query
/blog/<slug>→ blog_post()→ render_template('blog_post.html') + DB Lookup
/contact ──→ contact() ─→ render_template('contact.html')
/submit_contact (POST) ──→ save to DB, redirect back
```

---

## 💾 Database Schema

```
┌─────────────────────┐
│    Users Table      │
├─────────────────────┤
│ id (PK)             │
│ email (UNIQUE)      │
│ password_hash       │
│ created_at          │
└─────────────────────┘
         │
         │ 1:Many
         │
┌─────────────────────────────┐    ┌──────────────────────────────┐
│   Projects Table            │    │   BlogPosts Table            │
├─────────────────────────────┤    ├──────────────────────────────┤
│ id (PK)                     │    │ id (PK)                      │
│ title                       │    │ title                        │
│ description                 │    │ slug (UNIQUE)                │
│ technologies (CSV)          │    │ content                      │
│ github_url                  │    │ excerpt                      │
│ demo_url                    │    │ image_url                    │
│ image_url                   │    │ published_at                 │
│ created_at                  │    │ created_at                   │
└─────────────────────────────┘    └──────────────────────────────┘

┌───────────────────────────────────┐
│ ContactMessages Table             │
├───────────────────────────────────┤
│ id (PK)                           │
│ name                              │
│ email                             │
│ subject                           │
│ message                           │
│ created_at                        │
└───────────────────────────────────┘
```

---

## 📝 Template Inheritance

```
base.html (Master Template)
├── Navigation Bar
├── {% block content %}
│   ├── index.html (extends base.html)
│   ├── about.html (extends base.html)
│   ├── projects.html (extends base.html)
│   ├── blog.html (extends base.html)
│   ├── blog_post.html (extends base.html)
│   └── contact.html (extends base.html)
├── Footer
└── Scripts
```

**How it works:**
```
base.html provides: HTML structure, nav, footer, CSS/JS links
Child templates: Replace {% block content %} with their own HTML
Result: Consistent layout, no code repetition
```

---

## 🎨 Styling Cascade

```
CSS Cascade (top = highest priority):
│
├─ Inline Styles (fastest to apply)
│
├─ Custom CSS (static/css/style.css)
│   ├─ Classes (.card, .hero, .btn-custom)
│   ├─ IDs (#main-content)
│   └─ Element selectors (body, h1, p)
│
├─ Bootstrap Classes (5.3.0)
│   ├─ .container (width constraint)
│   ├─ .row / .col-* (grid)
│   ├─ .btn, .card (components)
│   └─ Utility classes (.mt-5, .text-center)
│
└─ Browser Defaults (buttons, links)
```

**Example:**
```html
<div class="card mt-5">        <!-- Bootstrap card + margin -->
  <div class="card-body">      <!-- Bootstrap body styling -->
    <h5 class="card-title">Title</h5>  <!-- Bootstrap + custom -->
  </div>
</div>
```

---

## 🔐 Security Layers

```
HTTPS (Automatic on Render.com)
    ↓
Input Validation (Form checks on frontend + backend)
    ↓
SQL Injection Prevention (SQLAlchemy handles this)
    ↓
XSS Protection (Jinja2 auto-escapes HTML)
    ↓
CSRF Tokens (Optional, for forms)
    ↓
Secure Password Storage (Use bcrypt when storing passwords)
    ↓
Environment Variables (.env file for secrets)
```

---

## 📈 Request-Response Timeline

```
Time(ms)   Event
─────────────────────────────────────
  0ms      User clicks link / types URL
 10ms      Browser connects to Render.com
 50ms      TLS handshake (HTTPS)
100ms      HTTP request arrives at server
150ms      Flask routes request to handler
200ms      Handler queries database
250ms      Database returns data
300ms      Jinja2 renders template
350ms      Response sent to browser
400ms      Browser starts rendering
500ms      HTML, CSS, JS loaded
600ms      Page interactive
```

---

## 🚀 Deployment Pipeline

```
┌─────────────────────────────────┐
│  Your Computer (Development)    │
│  ├─ Code files                  │
│  ├─ venv (Python environment)   │
│  ├─ SQLite database             │
│  └─ Flask dev server (port 5000)│
└──────────────┬──────────────────┘
               │ git push
               ↓
┌─────────────────────────────────┐
│     GitHub (Remote Repo)        │
│     ├─ Your code                │
│     ├─ Commit history           │
│     └─ Webhook to Render        │
└──────────────┬──────────────────┘
               │ GitHub triggers webhook
               ↓
┌─────────────────────────────────┐
│   Render.com Build Server       │
│  1. Clone repo from GitHub      │
│  2. Create Python environment   │
│  3. pip install requirements    │
│  4. Initialize database         │
│  5. Run migrations if any       │
│  6. Start gunicorn server       │
└──────────────┬──────────────────┘
               │ Deploy successful
               ↓
┌─────────────────────────────────┐
│   Render.com Production         │
│  ├─ Python runtime              │
│  ├─ Gunicorn web server         │
│  ├─ PostgreSQL option (later)   │
│  └─ HTTPS certificates (auto)   │
└──────────────┬──────────────────┘
               │ 
               ↓
┌─────────────────────────────────┐
│     User Browsers               │
│   https://yoursite.onrender.com │
└─────────────────────────────────┘
```

---

## 🔄 Contact Form Flow

```
1. User fills form on /contact page
   │
2. Form validation (HTML5 required attributes)
   │
3. User clicks Submit
   │
4. POST request to /submit_contact
   │
5. Server receives request
   ├─ Validates: name, email, subject, message all filled
   ├─ Validates: email format correct
   │
6. If validation FAILS:
   ├─ Render form again
   ├─ Show error messages
   ├─ Preserve user input (repopulate form)
   │
7. If validation PASSES:
   ├─ Create ContactMessage object
   ├─ Save to database
   ├─ Generate success message (flash message)
   ├─ Redirect to /contact (POST-Redirect-GET pattern)
   │
8. User sees success message
```

---

## 📊 MVC Pattern (Your Website Follows)

```
User Interaction
     ↓
┌─────────────────────┐
│  View (Templates)   │ ← HTML files, displays data
│  ├─ base.html       │
│  ├─ index.html      │
│  └─ projects.html   │
└──────────┬──────────┘
           │ User clicks
           ↓
┌─────────────────────┐
│ Controller (Routes) │ ← Flask app.py, handles requests
│ ├─ @app.route('/')  │
│ ├─ @app.route('/ab) │
│ └─ def projects()   │
└──────────┬──────────┘
           │ Fetches/updates
           ↓
┌─────────────────────┐
│ Model (Database)    │ ← SQLAlchemy models.py
│ ├─ Project          │
│ ├─ BlogPost         │
│ └─ ContactMessage   │
└──────────┬──────────┘
           │ Returns data
           ↓
         View renders
```

---

## ⚙️ Flask App Startup Process

```
1. python app.py executed
2. Import Flask library
3. Create Flask app instance: app = Flask(__name__)
4. Configure app:
   ├─ DATABASE_URI = 'sqlite:///personal_website.db'
   ├─ SECRET_KEY = secret
   └─ DEBUG = True (development)
5. Initialize extensions:
   ├─ SQLAlchemy: db = SQLAlchemy(app)
   └─ Others...
6. Define models:
   ├─ Import from database.models
   ├─ User, Project, BlogPost defined
   └─ Tables structure defined
7. Define routes:
   ├─ @app.route('/') → index()
   ├─ @app.route('/about') → about()
   └─ ... etc
8. if __name__ == '__main__':
   ├─ Create app context
   ├─ db.create_all()  (creates tables if not exist)
   ├─ app.run(debug=True)
9. Flask starts development server
10. "Running on http://localhost:5000"
11. Listening for requests...
```

---

## 📋 Checklist for Each Day

```
DAILY ROUTINE:
1. Start with: venv\Scripts\activate
2. Write code
3. Test frequently: python app.py
4. Commit progress: git add . && git commit -m "..."
5. Note any learnings
6. Move to next task

BEFORE BED:
- Did code run without errors?
- Did you test the changes?
- Is there a meaningful git commit?
- Do you understand what you built?
```

---

## 🎓 Key Concepts Summary

| Concept | What | Why | Where |
|---------|------|-----|-------|
| **Route** | URL → Function mapping | Organize different pages | app.py |
| **Template** | HTML with Python variables | Reuse layout, dynamic content | templates/ |
| **Model** | Database table structure | Store data persistently | models.py |
| **View Function** | Handles requests, returns responses | Process user input | app.py |
| **Jinja2** | Template language | Generate dynamic HTML | templates/ |
| **SQLAlchemy** | ORM (Object-Relational Map) | Python ↔ Database | models.py |
| **Bootstrap** | CSS framework | Professional responsive design | templates/ |
| **VENV** | Virtual environment | Isolated Python packages | /venv |
| **Git** | Version control | Track code changes | .git/ |
| **Render** | Cloud platform | Deploy app to internet | render.com |

---

## 🎯 Success Indicators

### ✅ Week 1 Success
- [ ] Flask app runs without crashing
- [ ] Database file created (personal_website.db)
- [ ] All routes respond (no 404s)
- [ ] Templates render with styling
- [ ] Contact form saves to database
- [ ] Navigation works between all pages
- [ ] Git history shows daily commits

### ✅ Week 2 Success
- [ ] Deployed to Render.com
- [ ] Live URL works from any browser
- [ ] Database queries show real data
- [ ] No errors in browser console
- [ ] Mobile responsive design works
- [ ] HTTPS shows as secure 🔒
- [ ] Performance acceptable

---

## 💪 You're Ready!

This visual guide provides quick reference to concepts you'll encounter. Bookmark this page!

**Next:** Read PROJECT_PLAN.md, then start WEEK_BY_WEEK.md Day 1!

