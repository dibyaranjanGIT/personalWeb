# Quick Start Guide

## 📚 Documentation Files Created

Here's everything you need to build your personal website:

| File | Purpose | When to Read |
|------|---------|--------------|
| **PROJECT_PLAN.md** | Complete 2-week overview, tech stack, success criteria | Start here first |
| **ARCHITECTURE.md** | System design, data flow, component breakdown | Before Week 1 Day 5 |
| **WEEK_BY_WEEK.md** | Detailed day-by-day breakdown with code examples | Your main guide |
| **DEPLOYMENT_GUIDE.md** | Step-by-step deployment to Render.com | Week 2 Day 12 |
| **This File** | Quick reference and checklist | Bookmark this |

---

## ⚡ Quick Start (Get Running in 10 Minutes)

### 1. Open PowerShell/Terminal

```powershell
cd c:\Users\dibya\Python\Personal\PersonalWebsite
```

### 2. Create Virtual Environment

```powershell
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```powershell
pip install Flask Flask-SQLAlchemy python-dotenv
```

### 4. Create app.py

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///personal_website.db'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return '<h1>Hello from Flask!</h1>'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

### 5. Run It!

```powershell
python app.py
```

Visit: http://localhost:5000

---

## 📋 Two-Week Timeline at a Glance

### Week 1: Build Foundation
```
Day 1-2: Environment setup, project structure, virtual environment
Day 3-4: Database models, Flask app, templates
Day 5-7: Create all 5 pages, add styling, test navigation
```

### Week 2: Deploy
```
Day 8-9: Add dynamic content from database
Day 10-11: Security, error handling, production config
Day 12-14: Deploy to Render.com, test, customize
```

---

## 📊 Tech Stack Reference

```
Frontend:
├─ HTML5 (templates)
├─ CSS3 (Bootstrap 5)
└─ JavaScript (vanilla)

Backend:
├─ Python 3.11+
├─ Flask (web framework)
└─ SQLAlchemy (ORM)

Database:
└─ SQLite (local development)

Deployment:
└─ Render.com (free tier)

Version Control:
└─ Git + GitHub
```

---

## 🎯 Success Checklist

### After Week 1, You Should Have:
```
✅ Flask app running locally
✅ SQLite database with sample data
✅ 5+ pages with Bootstrap styling
✅ Contact form working
✅ Navigation between all pages
✅ Code in GitHub with commits
```

### After Week 2, You Should Have:
```
✅ Website deployed to Render.com
✅ Live URL accessible from anywhere
✅ All features working in production
✅ Custom domain (optional)
✅ Professional portfolio website
```

---

## 📁 File Structure You'll Create

```
PersonalWebsite/
│
├── venv/                           # Virtual environment (don't commit)
├── static/
│   ├── css/style.css              # Your custom styles
│   ├── js/script.js               # Custom JavaScript
│   └── images/                    # Your photos
│
├── templates/
│   ├── base.html                  # Navigation, footer (inherited)
│   ├── index.html                 # Home page
│   ├── about.html                 # About page
│   ├── projects.html              # Portfolio
│   ├── blog.html                  # Blog listing
│   ├── contact.html               # Contact form
│   ├── blog_post.html             # Individual blog post
│   ├── 404.html                   # 404 error page
│   ├── 500.html                   # 500 error page
│   └── admin/
│       └── login.html             # Admin login
│
├── database/
│   ├── models.py                  # Database models
│   └── init_db.py                 # Sample data
│
├── app.py                         # Main Flask app
├── config.py                      # Configuration
├── requirements.txt               # Dependencies
├── Procfile                       # For Render deployment
├── runtime.txt                    # Python version
├── .env                           # Secrets (NEVER commit!)
├── .gitignore                     # What to ignore
├── personal_website.db            # Database (generated)
└── README.md                      # Project documentation
```

---

## 🔧 Common Commands

### Virtual Environment
```powershell
# Activate
venv\Scripts\activate

# Deactivate
deactivate
```

### Flask Development
```powershell
# Run development server
python app.py

# Run with specific port
set FLASK_ENV=development
python app.py
```

### Database
```powershell
# Initialize database
python -c "from app import app, db; app.app_context().push(); db.create_all()"

# Add sample data
python database/init_db.py
```

### Git
```powershell
# Check status
git status

# Commit changes
git add .
git commit -m "Your message"

# Push to GitHub
git push origin main
```

---

## 🐛 Troubleshooting

### "ModuleNotFoundError: No module named 'flask'"
```
Solution: Make sure venv is activated and requirements installed
venv\Scripts\activate
pip install -r requirements.txt
```

### "Address already in use"
```
Solution: Flask is already running, use different port
python -c "import sys; sys.argv = ['', '--port', '5001']; exec(open('app.py').read())"
```

### "Database is locked"
```
Solution: Close other connections to database, delete .db file to reset
del personal_website.db
python app.py
```

### "TemplateNotFound"
```
Solution: Check templates folder exists and file names are correct
ls templates/  # List template files
```

---

## 📚 Learning Resources by Topic

### Flask
- Official Docs: https://flask.palletsprojects.com/
- Real Python: https://realpython.com/flask-by-example/
- Video Tutorial: https://www.youtube.com/results?search_query=flask+tutorial

### Databases
- SQLAlchemy Docs: https://docs.sqlalchemy.org/
- SQL Basics: https://www.w3schools.com/sql/
- Database Design: https://en.wikipedia.org/wiki/Database_design

### Frontend
- Bootstrap Docs: https://getbootstrap.com/docs/
- HTML/CSS: https://www.w3schools.com/html/
- CSS Grid/Flexbox: https://css-tricks.com/

### Deployment
- Render Docs: https://render.com/docs
- Heroku (alternative): https://devcenter.heroku.com/
- GitHub Pages: https://pages.github.com/

---

## 💡 Pro Tips

### Tip 1: Use Chrome DevTools
- Right-click → Inspect Element
- View network requests
- Debug JavaScript
- Test responsive design

### Tip 2: Keep Git Commits Small
```bash
# ✅ Good commits (specific, focused)
git commit -m "Add home page hero section"
git commit -m "Create blog models and routes"

# ❌ Bad commits (too large, unclear)
git commit -m "update"
git commit -m "stuff"
```

### Tip 3: Test as You Build
- After each feature, test in browser
- Check browser console for errors
- Use Flask debug mode (debug=True locally)

### Tip 4: Use .env for Secrets
```python
# ❌ DON'T do this
SECRET_KEY = 'my-secret-12345'

# ✅ DO this
SECRET_KEY = os.getenv('SECRET_KEY')
```

### Tip 5: Comment Your Code
```python
# Describe why, not what
# ✅ Good: Skip deleted users to avoid confusion
users = User.query.filter(User.deleted=False).all()

# ❌ Bad: Loop through users
for user in users:
```

---

## 🎓 Learning Path

### Phase 1: Foundations (Days 1-4)
- Understand Python venv
- Learn Flask basics
- Setup database models
- Create first templates

### Phase 2: Building (Days 5-9)
- Create all pages
- Connect database to views
- Add form handling
- Understand Jinja2 thoroughly

### Phase 3: Production (Days 10-14)
- Security improvements
- Error handling
- Deployment process
- Production debugging

---

## ✅ Before You Start

Make sure you have:
- [ ] Python 3.8+ installed
- [ ] Visual Studio Code or editor
- [ ] Git installed
- [ ] GitHub account (free)
- [ ] Windows/Mac/Linux
- [ ] Internet connection
- [ ] Time commitment (2 weeks, 10-15 hours/week)

Check Python version:
```powershell
python --version
# Should show 3.8 or higher
```

---

## 🚀 Let's Build!

### Your Next Step:
1. Read **PROJECT_PLAN.md** (10 minutes)
2. Read **ARCHITECTURE.md** (15 minutes)
3. Follow **WEEK_BY_WEEK.md** starting Day 1

### Then:

**Day 1 Task:**
```
1. Create venv: python -m venv venv
2. Activate: venv\Scripts\activate
3. Install deps: pip install Flask Flask-SQLAlchemy python-dotenv
4. Create app.py with simple "Hello World"
5. Run: python app.py
6. Celebrate! 🎉
```

---

## 📞 When You Get Stuck

1. **Read Error Message Carefully** - It usually tells you exactly what's wrong
2. **Check the Docs** - Official documentation is your best friend
3. **Google It** - Chances are someone had the same problem
4. **Stack Overflow** - Search existing questions
5. **Try Simpler Code** - Start minimal, add complexity gradually
6. **Ask ChatGPT** - But verify the answer yourself

---

## 🎯 Your Mission

**Build a professional, deployed personal website in 2 weeks using Python, and understand every part of it.**

### Why This Matters:
- ✅ Portfolio piece for job applications
- ✅ Deep understanding of web development
- ✅ Hands-on experience with real deployment
- ✅ Confidence to build more projects
- ✅ Professional web presence

---

## 📊 Progress Tracking

Track your daily progress:

```markdown
# Progress Tracker

## Week 1
- [ ] Day 1: Environment setup
- [ ] Day 2: Database models
- [ ] Day 3-4: Templates
- [ ] Day 5-7: Core pages

## Week 2
- [ ] Day 8-9: Dynamic content
- [ ] Day 10-11: Production prep
- [ ] Day 12-14: Deployment
```

---

## 🎉 Celebrate Milestones

- ✨ Day 1: First Flask app running
- ✨ Day 2: Database working
- ✨ Day 4: Website has styling
- ✨ Day 7: All pages working
- ✨ Day 9: Database content showing
- ✨ Day 11: Security implemented
- ✨ Day 14: **LIVE ON INTERNET!** 🚀

---

## Final Thoughts

You're about to build something amazing. Take it step by step, don't rush, and most importantly - **enjoy the learning process!**

The fact that you're learning to build things, not just use them, is what matters. Every developer started exactly where you are now.

### Remember:
- Code is meant to be broken and fixed
- Errors are learning opportunities
- Your progress is what matters, not perfection
- You're building valuable skills

---

**Let's do this! 💪**

**Questions? Check PROJECT_PLAN.md, ARCHITECTURE.md, or WEEK_BY_WEEK.md**

**Ready? Start with Day 1 in WEEK_BY_WEEK.md!**
