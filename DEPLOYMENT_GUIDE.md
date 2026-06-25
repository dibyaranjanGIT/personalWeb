# Free Deployment Guide

## 🎯 Why Render.com?

| Feature | Render.com | PythonAnywhere | Heroku |
|---------|-----------|----------------|--------|
| **Free Tier** | ✅ Generous | ✅ Limited | ❌ Removed |
| **Python Support** | ✅ Excellent | ✅ Excellent | ✅ Not available |
| **Ease of Use** | ✅ Very Easy | ⚠️ Medium | ⚠️ Complex |
| **Git Integration** | ✅ Auto-deploy | ❌ Manual upload | ✅ Via CLI |
| **Cost** | 💰 $0-7/mo | 💰 $5/mo | ❌ Paid only |
| **Custom Domain** | ✅ Yes (free) | ✅ Yes | ✅ Yes |
| **Sleep Mode** | ⏸️ After 15 min | ✅ No sleep | N/A |
| **Recommendation** | 🥇 BEST | 🥈 Good | ❌ Skip |

---

## 🚀 Step-by-Step Deployment Guide

### Phase 1: Prepare Your Application (Week 2, Days 10-11)

#### Step 1: Create `.env` File

Create `.env` in your project root:

```env
FLASK_ENV=production
SECRET_KEY=your-super-secret-key-here-make-it-random
DATABASE_URL=sqlite:///personal_website.db
DEBUG=False
```

⚠️ **IMPORTANT**: Add to `.gitignore` so it never commits to GitHub:

```gitignore
.env
*.db
__pycache__/
venv/
.DS_Store
```

#### Step 2: Create `requirements.txt`

```txt
Flask==3.0.0
Flask-SQLAlchemy==3.1.1
python-dotenv==1.0.0
gunicorn==21.2.0
email-validator==2.0.0
Werkzeug==3.0.0
```

#### Step 3: Create `Procfile`

Tells Render how to run your app:

```
web: gunicorn app:app
```

#### Step 4: Update `app.py`

Add configuration handling:

```python
import os
from dotenv import load_dotenv

load_dotenv()

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-key-change-me')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///personal_website.db')
app.config['DEBUG'] = os.getenv('DEBUG', False)

if __name__ == '__main__':
    app.run(debug=False)  # Never True in production
```

#### Step 5: Push to GitHub

```bash
git add .
git commit -m "Prepare for deployment"
git push origin main
```

---

### Phase 2: Setup on Render.com (Week 2, Days 12-13)

#### Step 1: Create Render Account

1. Go to https://render.com
2. Click "Get Started" (sign up with GitHub)
3. Authorize GitHub access
4. Complete profile

#### Step 2: Create New Web Service

1. Dashboard → "New +" → "Web Service"
2. Select your GitHub repository
3. Configure settings:

   ```
   Name: personal-website
   Environment: Python 3
   Build Command: pip install -r requirements.txt
   Start Command: gunicorn app:app
   ```

4. Plan: Select "Free"
5. Click "Create Web Service"

#### Step 3: Configure Environment Variables

In Render Dashboard:

1. Go to your Web Service
2. Settings → Environment
3. Add these variables:

   ```
   KEY                VALUE
   FLASK_ENV          production
   SECRET_KEY         [random-32-char-string]
   DEBUG              False
   ```

**To generate SECRET_KEY**, run in Python:

```python
import secrets
print(secrets.token_hex(32))
```

#### Step 4: Deploy

When you push to GitHub, Render automatically:
1. Pulls latest code
2. Installs dependencies
3. Runs build command
4. Starts your app

View logs in Render dashboard to debug any issues.

---

## 📋 Deployment Checklist

### Before Deployment

- [ ] `.env` file created and added to `.gitignore`
- [ ] `requirements.txt` contains all dependencies
- [ ] `Procfile` created
- [ ] `app.py` reads environment variables
- [ ] `DEBUG=False` in production config
- [ ] Database schema properly defined
- [ ] All code committed to GitHub
- [ ] README.md written with setup instructions

### On Render.com

- [ ] Web Service created
- [ ] Environment variables configured
- [ ] Deployment successful (check logs)
- [ ] Website loads without errors
- [ ] Database initialized (may need manual trigger)
- [ ] All pages working
- [ ] Contact form functional

### Post-Deployment

- [ ] Test all pages
- [ ] Test contact form
- [ ] Check performance
- [ ] Review logs for errors
- [ ] Set up custom domain (optional)

---

## 🆓 Free Tier Limitations & Workarounds

### Render.com Free Tier

| Limitation | Details | Workaround |
|-----------|---------|-----------|
| **Spin-down** | Service stops after 15 min inactivity | Acceptable for portfolio |
| **Startup time** | 30-50 sec cold start | Add uptime monitor |
| **Resources** | 0.5 CPU, 512MB RAM | Sufficient for low traffic |
| **Storage** | Limited (SQLite only) | Upgrade to PostgreSQL if needed |
| **Bandwidth** | Limited | Add CDN if needed |

### How to Avoid Spin-downs

Use a free uptime monitor:

1. Go to https://uptimerobot.com
2. Create free account
3. Add new monitor (choose "HTTP(s)")
4. URL: Your Render domain
5. Interval: 5-10 minutes

This keeps your site awake! ✨

---

## 🔧 Common Issues & Solutions

### Issue 1: "Error building application"

**Check:**
- Missing `requirements.txt`
- Syntax errors in Python files
- Missing dependencies listed

**Solution:**
```bash
pip freeze > requirements.txt  # Include ALL dependencies
```

### Issue 2: "Application failed to start"

**Check in Render Logs:**
```
1. Look for specific error messages
2. Check if database file is created
3. Verify environment variables set
```

**Common Fix:**
```python
# Ensure app starts without database
app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', False)
```

### Issue 3: "Module not found" error

**Solution:**
```bash
# Make sure ALL dependencies in requirements.txt
pip freeze > requirements.txt
```

### Issue 4: Database errors

**Solution:**
Add initialization code in `app.py`:

```python
with app.app_context():
    db.create_all()  # Creates tables if they don't exist
```

---

## 📊 Monitoring Your Deployment

### Render Dashboard

- **Logs**: Real-time application output
- **Metrics**: CPU, memory, network usage
- **Deployments**: History of all deployments
- **Events**: Restarts, build failures

### Check Logs Regularly

1. Render Dashboard → Your Service → Logs
2. Look for errors: `ERROR`, `Exception`, `Traceback`
3. Debug using error messages

### Email Alerts (Optional)

Render can email you on deployment failures:
- Settings → Notification Rules
- Choose "Failure" events
- Add your email

---

## 🔐 Security for Deployment

### Never Commit Secrets

❌ **BAD:**
```python
SECRET_KEY = 'my-super-secret-key-12345'  # Don't do this!
```

✅ **GOOD:**
```python
SECRET_KEY = os.getenv('SECRET_KEY')  # Read from .env
```

### HTTPS (Automatic)

- ✅ All Render domains use HTTPS
- ✅ SSL certificate auto-renewed
- ✅ Redirects HTTP to HTTPS

### Secure Headers

Add to your Flask app:

```python
@app.after_request
def set_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response
```

---

## 🎯 Custom Domain (Optional, Week 2 Day 14)

### Use Free Domain

Option 1: Keep Render subdomain
- Your URL: `yourname.onrender.com`
- ✅ Free, auto SSL, easy

Option 2: Buy cheap domain ($3-10/year)
- Providers: Namecheap, GoDaddy, Google Domains
- ✅ More professional

### Connect Custom Domain on Render

1. Dashboard → Custom Domains
2. Add Domain
3. Update DNS records (Render shows instructions)
4. Wait 24-48 hours for DNS propagation

---

## 📈 Scaling Beyond Free Tier

If your site gets popular:

### Step 1: Upgrade Plan ($7/month)
- Paid tier on Render
- No spin-downs
- Better resources

### Step 2: Upgrade Database
- Move from SQLite to PostgreSQL
- Better for multi-user access
- Render PostgreSQL: $15/month

### Step 3: Add Caching
- Redis cache layer
- Faster page loads
- Render Redis: $5/month

### Step 4: CDN
- Cloudflare (free tier)
- Serve static files faster globally

---

## ✅ Deployment Success Checklist

### Your site is ready when:

- [ ] Accessible via URL (render.onrender.com or custom domain)
- [ ] All pages load correctly
- [ ] Styling looks good
- [ ] Contact form works
- [ ] Database queries functional
- [ ] No error messages in browser
- [ ] Responsive on mobile
- [ ] HTTPS shows as secure 🔒
- [ ] Performance is acceptable

---

## 🎓 What You've Learned

After deployment, you understand:

✅ Environment configuration
✅ Production vs development
✅ Secret management
✅ Cloud deployment basics
✅ Monitoring and logs
✅ Scaling considerations
✅ Security best practices
✅ DevOps fundamentals

**Congratulations! Your app is live! 🚀**

---

## 📚 Helpful Links

- Render Documentation: https://render.com/docs
- Flask Deployment: https://flask.palletsprojects.com/deployment/
- UptimeRobot: https://uptimerobot.com
- Namecheap (Domain): https://www.namecheap.com

---

**Next Step: Start building! Let's begin with Week 1! 📝**
