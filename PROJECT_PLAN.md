# Personal Website - Complete Project Plan

## 📋 Overview
Build a professional personal website using Python in 2 weeks, with a focus on learning and understanding each component.

**Timeline**: 2 Weeks (April 25 - May 9, 2026)
**Tech Stack**: Python, Flask, SQLite, Bootstrap, Render.com

---

## 🎯 Project Goals

1. ✅ Create a personal portfolio/resume website
2. ✅ Learn web development fundamentals
3. ✅ Understand server-side rendering with Python
4. ✅ Deploy to production on free tier
5. ✅ Implement database interactions
6. ✅ Add dynamic content features

---

## 📦 Tech Stack Explanation

### Why These Choices?

| Component | Choice | Why |
|-----------|--------|-----|
| **Backend Framework** | Flask | Lightweight, Pythonic, perfect for learning |
| **Database** | SQLite | No server needed, built-in Python support, free |
| **Frontend** | HTML + Bootstrap | Responsive design, minimal setup, focus on backend |
| **Deployment** | Render.com | Free tier, easy deployment, Python-friendly |
| **Version Control** | Git + GitHub | Industry standard, backup, portfolio piece |

---

## 🏗️ Architecture Overview

```
PersonalWebsite/
├── app.py                    # Main Flask application
├── config.py                 # Configuration settings
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (never commit)
├── .gitignore               # Git ignore rules
│
├── static/                   # Static files (CSS, JS, images)
│   ├── css/
│   │   └── style.css        # Custom styling
│   ├── js/
│   │   └── script.js        # Custom JavaScript
│   └── images/
│       └── profile.jpg      # Your profile picture
│
├── templates/                # HTML templates
│   ├── base.html            # Base template (navigation, footer)
│   ├── index.html           # Home page
│   ├── about.html           # About page
│   ├── projects.html        # Projects portfolio
│   ├── blog.html            # Blog listing
│   ├── contact.html         # Contact form
│   └── admin/               # Admin panel templates
│       ├── login.html
│       └── dashboard.html
│
├── database/                 # Database-related files
│   └── init_db.py           # Database initialization
│
├── venv/                     # Virtual environment (ignored in git)
│
└── README.md                # Project documentation
```

---

## 📊 Database Schema

### Simple Structure (3 tables)

```
Users Table:
- id (PRIMARY KEY)
- email (UNIQUE)
- password_hash
- created_at

Projects Table:
- id (PRIMARY KEY)
- title
- description
- technologies (comma-separated)
- github_url
- demo_url
- image_url
- created_at

Blog Posts Table:
- id (PRIMARY KEY)
- title
- slug (URL-friendly)
- content
- excerpt
- image_url
- published_at
- created_at
```

---

## 🚀 Week-by-Week Breakdown

### **Week 1: Foundation & Setup**

#### Day 1-2: Environment Setup
- [ ] Create project directory structure
- [ ] Set up Python virtual environment
- [ ] Initialize Git repository
- [ ] Create requirements.txt with dependencies
- [ ] Setup Flask application scaffold
- **Learning Focus**: Python venv, pip, Flask basics

#### Day 3-4: Database & Static Files
- [ ] Create SQLite database schema
- [ ] Build Bootstrap-based templates structure
- [ ] Create base.html with navigation
- [ ] Add CSS styling
- **Learning Focus**: SQL, Jinja2 templating, CSS

#### Day 5-7: Core Pages
- [ ] Build Home page (index.html)
- [ ] Create About page
- [ ] Setup Contact form (basic)
- [ ] Add simple styling
- [ ] Test locally
- **Learning Focus**: Flask routing, template inheritance, forms

---

### **Week 2: Features & Deployment**

#### Day 8-9: Advanced Features
- [ ] Build Projects portfolio page
- [ ] Create Blog listing page
- [ ] Simple admin login (optional)
- [ ] Contact form submission (email or database)
- **Learning Focus**: Database queries, user authentication basics

#### Day 10-11: Production Preparation
- [ ] Environment configuration (.env)
- [ ] Error handling & logging
- [ ] Security setup (CSRF protection, secure headers)
- [ ] Performance optimization (minify CSS/JS)
- **Learning Focus**: Security, deployment readiness

#### Day 12-14: Deployment & Testing
- [ ] Create Render.com account
- [ ] Deploy application
- [ ] Setup custom domain (optional)
- [ ] Test all features in production
- [ ] Final polish and tweaks
- **Learning Focus**: DevOps basics, deployment process

---

## 💾 Deployment Options (Free Tier)

### 🥇 Recommended: **Render.com**
- **Pros**: Easy Flask deployment, automatic git sync, free tier generous
- **Cons**: Free tier sleeps after 15 min inactivity (acceptable for portfolio)
- **Steps**: Push to GitHub → Connect Render.com → Done!
- **Cost**: Free (with limitations)

### 🥈 Alternative 1: **PythonAnywhere**
- **Pros**: Python-specific, easy setup, good documentation
- **Cons**: Limited free tier features
- **Cost**: Free with limited resources

### 🥉 Alternative 2: **Heroku (Deprecated) → Use Render Instead**
- **Note**: Heroku removed free tier, use Render instead

### 🔄 Alternative 3: **Railway or Vercel**
- **Pros**: Modern, fast deployment
- **Cons**: Limited free tier
- **Cost**: Free trial, then paid

**We'll use Render.com** - best balance of ease and features.

---

## 🔧 Key Python Packages

```
Flask==3.0.0              # Web framework
Flask-SQLAlchemy==3.1.1   # Database ORM
Flask-Migrate==4.0.5      # Database migrations
python-dotenv==1.0.0      # Environment variables
gunicorn==21.2.0          # Production server
email-validator==2.0.0    # Email validation
```

---

## 📝 Learning Path

By the end of 2 weeks, you'll understand:

1. **Python Web Basics**: Flask routing, app structure
2. **Templating**: Jinja2, template inheritance, loops
3. **Databases**: SQL basics, CRUD operations, SQLite
4. **HTML/CSS**: Semantic HTML, responsive design with Bootstrap
5. **Forms**: Form handling, validation, submission
6. **Deployment**: Git workflow, environment configuration, cloud deployment
7. **Security**: Password hashing, CSRF protection, secure headers

---

## 🛠️ Tools You'll Use

- **VS Code**: Code editor
- **Git/GitHub**: Version control
- **Render.com**: Hosting
- **SQLite Browser**: Database visualization (optional)
- **Postman**: API testing (optional, for later improvements)

---

## ✨ Future Enhancements (After 2 Weeks)

- [ ] Add comment system for blog posts
- [ ] Email notifications for contact forms
- [ ] Search functionality
- [ ] Dark mode toggle
- [ ] Analytics integration
- [ ] API for external consumption
- [ ] Progressive Web App (PWA) features
- [ ] CI/CD pipeline with GitHub Actions

---

## 📚 Resources We'll Reference

- Flask Official Docs: https://flask.palletsprojects.com/
- Render Deployment: https://render.com/docs
- Bootstrap Docs: https://getbootstrap.com/docs/5.0/
- Jinja2 Templating: https://jinja.palletsprojects.com/

---

## ✅ Success Criteria

By the end of Week 2, you should have:

1. ✅ Fully functional website with 5+ pages
2. ✅ Database storing projects and/or blog posts
3. ✅ Working contact form
4. ✅ Deployed and accessible via URL
5. ✅ Clean, responsive design
6. ✅ GitHub repository with commit history
7. ✅ Understanding of each component built

---

**Ready to start? Let's begin with Week 1! 🚀**
