# Architecture Document

## 🏗️ System Architecture

### High-Level Overview

```
┌─────────────────────────────────────────────────────────────┐
│                     USER BROWSER                            │
│                   (Client Side)                             │
└────────────────────────┬────────────────────────────────────┘
                         │
                    HTTP/HTTPS
                         │
         ┌───────────────┴───────────────┐
         │                               │
         ▼                               ▼
    ┌─────────────┐          ┌─────────────────────┐
    │  Static     │          │  Flask App Server   │
    │   Files     │          │  (app.py)           │
    │  (CSS, JS)  │          │                     │
    │  (Images)   │          │  Routes:            │
    └─────────────┘          │  - / (home)         │
                             │  - /about           │
                             │  - /projects        │
                             │  - /blog            │
                             │  - /contact         │
                             │  - /admin (login)   │
                             └─────────┬───────────┘
                                       │
                                       ▼
                             ┌─────────────────────┐
                             │   SQLite Database   │
                             │                     │
                             │ - Users             │
                             │ - Projects          │
                             │ - Blog Posts        │
                             │ - Contact Messages  │
                             └─────────────────────┘
```

### Application Flow

```
User Request
     │
     ▼
Flask Route Handler
     │
     ├─► Database Query (if needed)
     │        │
     │        ▼
     │   SQLite DB
     │        │
     │        ▼
     │   Data returned
     │
     ▼
Render Template (Jinja2)
     │
     ├─► Load HTML template
     ├─► Insert dynamic data
     ├─► Include static files (CSS, JS)
     │
     ▼
HTTP Response
     │
     ▼
Browser Renders Page
```

---

## 🔄 Component Breakdown

### 1. **Frontend (Client-Side)**
- **HTML Templates** (Jinja2)
  - Base template with navigation/footer
  - Page-specific templates
  - Form templates
  
- **CSS** (Bootstrap + Custom)
  - Responsive layout
  - Color scheme, typography
  - Component styling
  
- **JavaScript** (Vanilla + Bootstrap JS)
  - Form validation
  - Interactive elements
  - Smooth scrolling

### 2. **Backend (Server-Side) - Flask**
- **Routes & Views**
  - URL routing
  - Request handling
  - Data processing
  
- **Database Models**
  - User model
  - Project model
  - BlogPost model
  
- **Business Logic**
  - Authentication
  - Form processing
  - Email sending

### 3. **Database - SQLite**
- **Persistence**
  - Store projects, blog posts
  - User credentials
  - Contact submissions
  
- **Relationships**
  - User → Projects
  - User → Blog Posts

### 4. **Deployment - Render.com**
- **Environment**
  - Python runtime
  - Environment variables
  - Build process
  
- **Monitoring**
  - Logs
  - Error tracking
  - Performance metrics

---

## 📊 Request-Response Cycle

### Example: Loading Home Page

```
1. User types: https://mywebsite.com/
   │
2. Browser sends: GET / HTTP/1.1
   │
3. Render receives request → routes to Flask app
   │
4. Flask matches route: @app.route('/')
   │
5. Handler function executes:
   - Fetch featured projects from database
   - Fetch recent blog posts
   │
6. Render template: render_template('index.html', projects=..., posts=...)
   │
7. Template engine processes:
   - Fills {% variables %}
   - Loops through {% for post in posts %}
   - Includes CSS/JS links
   │
8. Server sends: HTML + CSS + JS
   │
9. Browser receives and renders page
   │
10. User sees: Beautifully formatted personal website
```

---

## 🔐 Security Architecture

### Layers of Security

```
┌──────────────────────────────────────────┐
│  1. HTTPS/TLS Encryption                 │ ← Transit security
│     (Automatic on Render.com)             │
└──────────────────────────────────────────┘
                 ▼
┌──────────────────────────────────────────┐
│  2. Input Validation & Sanitization      │ ← Data integrity
│     - Form validation                     │
│     - SQL injection prevention            │
│     - XSS protection                      │
└──────────────────────────────────────────┘
                 ▼
┌──────────────────────────────────────────┐
│  3. Authentication & Authorization       │ ← Access control
│     - Secure password hashing (bcrypt)   │
│     - Session management                 │
│     - CSRF tokens on forms               │
└──────────────────────────────────────────┘
                 ▼
┌──────────────────────────────────────────┐
│  4. Environment Configuration            │ ← Secret management
│     - .env file (never commit)           │
│     - Secret keys in Render dashboard    │
│     - No sensitive data in code          │
└──────────────────────────────────────────┘
```

---

## 📁 File Organization Rationale

```
PersonalWebsite/
├── app.py                  # Central entry point - easy to locate
├── config.py              # All settings in one place - single responsibility
├── requirements.txt       # Dependencies clearly documented
│
├── static/               # Served directly by web server (fast)
│   ├── css/              # Static assets don't need server processing
│   ├── js/
│   └── images/
│
├── templates/            # HTML files processed by Flask/Jinja2
│   ├── base.html         # DRY principle - shared layout
│   └── admin/            # Organize by feature
│
├── database/             # Database logic grouped together
│   └── init_db.py        # Easy to reset/initialize
│
└── venv/                 # Isolated environment (git ignored)
```

---

## 🔄 Data Flow Example: Contact Form

```
User fills contact form on /contact page
     │
     ▼
Browser sends POST request to /submit_contact
     │
     ▼
Flask receives request:
  - Validates form data
  - Checks for empty fields
  - Validates email format
     │
     ├─ Validation FAILS ──► Render form with errors ──► User sees error messages
     │
     └─ Validation PASSES ──► Continue
                             │
                             ▼
                       Save to database OR Send email
                             │
                             ▼
                       Redirect to success page
                             │
                             ▼
                       User sees confirmation
```

---

## ⚡ Performance Considerations

### Optimization Strategy

1. **Static File Caching**
   - CSS/JS minified
   - Browser caching headers
   - CDN-ready (future)

2. **Database Optimization**
   - Indexes on frequently queried columns
   - Limit queries to necessary fields
   - Use pagination for large lists

3. **Template Efficiency**
   - Avoid N+1 queries
   - Cache computed data
   - Minimize template complexity

4. **Render.com Specifics**
   - Free tier: short startup time acceptable
   - Use gunicorn for production server
   - Monitor memory usage

---

## 🚀 Deployment Architecture

### Local Development
```
Your Computer
    │
    ├─ VS Code
    ├─ Python venv
    ├─ SQLite DB (local)
    └─ Flask dev server (http://localhost:5000)
```

### Production on Render.com
```
Render.com Infrastructure
    │
    ├─ Git integration (auto-deploy on push)
    ├─ Python environment setup
    ├─ Install dependencies (pip install -r requirements.txt)
    ├─ Initialize database
    ├─ Run gunicorn server
    └─ Serve on https://yoursite.onrender.com
```

### Deployment Steps Visualization

```
1. Code committed to GitHub
           │
2. Push to main branch
           │
3. Webhook triggers Render
           │
4. Render pulls latest code
           │
5. Build environment:
   - Install Python
   - Create venv
   - pip install requirements
   - Run migrations
           │
6. Start application:
   - gunicorn app:app
           │
7. Application live on internet!
```

---

## 📊 Scalability Considerations (Phase 2)

### Current Architecture (Week 2)
- ✅ Single server
- ✅ SQLite database
- ✅ Minimal traffic

### Future Improvements (After Phase 1)
- 🔄 Upgrade to PostgreSQL (if data grows)
- 🔄 Add caching layer (Redis)
- 🔄 CDN for static files (Cloudflare)
- 🔄 Background jobs (Celery + Redis)
- 🔄 Database backups automation

---

## 🎯 Architecture Principles Used

1. **Separation of Concerns**: Routes, database, templates separate
2. **DRY (Don't Repeat Yourself)**: Base template, reusable components
3. **Modularity**: Easy to add features without breaking existing code
4. **Security First**: Input validation, CSRF protection built-in
5. **Performance**: Static files served fast, database queries optimized
6. **Scalability**: Structure allows easy upgrade path

---

**This architecture is designed to be simple to learn but strong enough for a professional portfolio! 🎓**
